library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Neuron_FB_alt is
    generic(
        N_FF:       positive := 4;
        N_FB:       positive := 2;
        N_syn:      positive := 4);
    Port(
        NeuronIn:   in std_logic_vector(0 to N_syn-1);
        clk:        in std_logic;
        rst:        in std_logic;
        NeuronOut:  out std_logic;
        check_ff:   out std_logic_vector(0 to N_FF-1); -- Delete later. For Debugging.
        check_fb:   out std_logic_vector(0 to N_FB-1); -- Delete later. For Debugging.
        check_xor:  out std_logic; -- Delete later. For Debugging.
        check_or:   out std_logic -- Delete later. For Debugging.
        );
end Neuron_FB_alt;

architecture sync_FB_register of Neuron_FB_alt is
signal ff_reg:  std_logic_vector(0 to N_FF-1) := (others => '0');
signal fb_reg:  std_logic_vector(0 to N_FB-1) := (others => '0');
signal or_temp: std_logic_vector(0 to N_syn-1) := (others => '0');
signal or_out: std_logic := '0';
signal xor_out: std_logic := '0';

begin
    or_temp(0) <= NeuronIn(0);
    inputGen: for i in 1 to (N_syn-1) generate
        or_temp(i) <= or_temp(i-1) OR NeuronIn(i);
    end generate inputGen;
    
    xor_out <= or_temp(N_Syn-1) XOR fb_reg(N_FB-1);
    NeuronOut <= ff_reg(N_FF-1);
    
    feedforward_process: process (clk, rst)
    begin
        if(rst = '1') then
                ff_reg <= (others => '0');
                fb_reg <= (others => '0');
        elsif(rising_edge(clk) and fb_reg(N_FB-1) = '0') then
            ff_reg <= xor_out & ff_reg(0 to (N_FF-2));
            fb_reg <= ff_reg(N_FF-1) & fb_reg(0 to (N_FB-2));
        elsif(rising_edge(clk) and fb_reg(N_FB-1) = '1') then
            ff_reg <= xor_out & ff_reg(0 to (N_FF-2));
--            fb_reg <= (others => '0'); -- Full Reset
            fb_reg <= (0 => ff_reg(N_FF-1), others => '0'); -- Partial Reset
        end if;
    end process feedforward_process;
    
    check_ff <= ff_reg;                         -- Delete later. For Debugging.
    check_fb <= fb_reg;                         -- Delete later. For Debugging.
    check_xor <= xor_out;                       -- Delete later. For Debugging.
    check_or <= or_temp(N_Syn-1);               -- Delete later. For Debugging.
end sync_FB_register;
