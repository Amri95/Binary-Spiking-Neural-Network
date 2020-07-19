library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.std_logic_textio.all;
use STD.textio.all;

entity neurons_tb is
--  Port ( );
end neurons_tb;

architecture Behavioral of neurons_tb is
component Neuron_FB_alt is
generic(
    N_FF:       positive := 4;
    N_FB:       positive := 2;
    N_syn:      positive := 4);
Port(
    NeuronIn:   in std_logic_vector(0 to N_syn-1);
    clk:        in std_logic;
    rst:        in std_logic;
    NeuronOut:  out std_logic
    );
end component Neuron_FB_alt;

constant ff_reg_size: positive := 4;
constant fb_reg_size: positive := 2;
constant Num_inputs: positive := 1;
constant period : time := 2000 ps;

signal SIn: std_logic_vector(0 to Num_inputs-1) := (others =>'0');
signal clk: std_logic := '0';
signal rst: std_logic := '0';
signal SOut: std_logic;
signal fin: std_logic := '0';

begin
    neuron1: Neuron_FB_alt
    generic map(N_FF => ff_reg_size, N_FB => fb_reg_size, N_syn => Num_inputs)
    port map(
        NeuronIn => SIn, clk => clk, rst => rst, NeuronOut => SOut,
        check_xor => check_xor, check_or => check_or);
    
    clk <= not clk after period/2;
    
    test_process: process (clk)
    variable v_iline     : line;
    variable v_oline     : line;
    variable input_vector: std_logic_vector(0 to Num_inputs-1);
    file file_neuron_out      : text open write_mode is "vhdl_NeuronOutMultFreq0.01_part_reset.txt";
    file file_vectors      : text open read_mode is "neuron_input_multiple_frequencies0.01.txt";
    
    begin
        if(rising_edge(clk) and not endfile(file_vectors)) then
            readline(file_vectors, v_iline);
            read(v_iline, input_vector);
            
            SIn <= input_vector;
            write(v_oline, SOut, left, 1);
            writeline(file_neuron_out, v_oline);
        elsif(endfile(file_vectors)) then
            file_close(file_vectors);
            file_close(file_neuron_out);
        end if;
        
    end process test_process;
    
    reset_process: process
    begin
        wait for 200ps;
        rst <= '1';
        wait for 200ps;
        rst <= '0';
        wait for 9999.6ns;
    end process reset_process;
end Behavioral;
