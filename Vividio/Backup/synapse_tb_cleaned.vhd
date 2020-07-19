library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.std_logic_textio.all;
use STD.textio.all;


entity synapse_tb is
--  Port ( );
end synapse_tb;

architecture Behavioral of synapse_tb is
component Synapse is
    generic(
        n:  positive := 16);
    Port(
        synIn:  in std_logic;
        clk:    in std_logic;
        rst:  in std_logic;
        synOut: out std_logic;
        p_data: in std_logic_vector(0 to n-1)
	  );
end component Synapse;

constant N: positive := 16;
constant period: time := 2000ps;
signal SIn: std_logic := '0';
signal clk: std_logic := '0';
signal rst: std_logic := '0';
signal SOut: std_logic;
signal reg_data: std_logic_vector(0 to N-1):= "1111010111010100";

begin
    test_synapse: Synapse
    generic map(n => N)
    port map(synIn => SIn, clk => clk, rst => rst, synOut => SOut, p_data => reg_data);
    
    clk <= not clk after period/2;
    
    test_process: process(clk)
    variable v_iline     : line;
    variable v_oline     : line;
    variable input_vector: std_logic;
    file file_synapse_out      : text open write_mode is "vhdl_synapse_output.txt";
    file file_vectors      : text open read_mode is "synapse_input_vector.txt";
    
    begin
        if(rising_edge(clk) and not endfile(file_vectors)) then
            readline(file_vectors, v_iline);
            read(v_iline, input_vector);
            
            SIn <= input_vector;
            write(v_oline, SOut, left, 1);
            writeline(file_synapse_out, v_oline);
        elsif(endfile(file_vectors)) then
            file_close(file_vectors);
            file_close(file_synapse_out);
        end if;
    end process test_process;
        reset_process: process
    begin
        wait for 100ps;
        rst <= '1';
        wait for 100ps;
        rst <= '0';
        wait for 18000ns;
    end process reset_process;

end Behavioral;
