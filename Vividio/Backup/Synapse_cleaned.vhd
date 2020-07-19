library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Synapse is
    generic(
        n:  positive := 16);
    Port(
        synIn:  in std_logic;
        clk:    in std_logic;
        rst:  in std_logic;
        synOut: out std_logic;
        p_data: in std_logic_vector(0 to n-1);
	  );
end Synapse;

architecture sync_arch of Synapse is
signal shift_reg: std_logic_vector(0 to n-1):= (others => '0');
begin
    synOut <= shift_reg(0) and synIn;
    shift: process(clk, rst)
    begin
        if(rst = '1') then
            shift_reg <= p_data;
        elsif(rising_edge(clk)) then
                shift_reg <= shift_reg(n-1) & shift_reg(0 to n-2);
        end if;
    end process shift;
end sync_arch;
