-- fsm.vhd: Finite State Machine
-- Author(s): 
--
library ieee;
use ieee.std_logic_1164.all;
-- ----------------------------------------------------------------------------
--                        Entity declaration
-- ----------------------------------------------------------------------------
entity fsm is
port(
   CLK         : in  std_logic;
   RESET       : in  std_logic;

   -- Input signals
   KEY         : in  std_logic_vector(15 downto 0);
   CNT_OF      : in  std_logic;

   -- Output signals
   FSM_CNT_CE  : out std_logic;
   FSM_MX_MEM  : out std_logic;
   FSM_MX_LCD  : out std_logic;
   FSM_LCD_WR  : out std_logic;
   FSM_LCD_CLR : out std_logic
);
end entity fsm;

-- ----------------------------------------------------------------------------
--                      Architecture declaration
-- ----------------------------------------------------------------------------
architecture behavioral of fsm is
   type t_state is (DEFAULT, CASE_ERROR, CASE_CORRECT,
						CASE_1 , CASE_5, CASE_3,
						CASE1_4, CASE1_81, CASE1_82, CASE1_6, CASE1_5, CASE1_0, 
						CASE2_7, CASE2_9, CASE2_21, CASE2_0, CASE2_22, CASE2_23, 
						PRINT_ERROR, PRINT_CORRECT, FINISH);
   signal present_state, next_state : t_state;

begin
-- -------------------------------------------------------
sync_logic : process(RESET, CLK)
begin
   if (RESET = '1') then
      present_state <= DEFAULT;
   elsif (CLK'event AND CLK = '1') then
      present_state <= next_state;
   end if;
end process sync_logic;

-- -------------------------------------------------------
next_state_logic : process(present_state, KEY, CNT_OF)
begin
   case (present_state) is
   -- - - - - - - - - - - - - - - - - - - - - - -
   when DEFAULT =>
      next_state <= DEFAULT;
		if (KEY(1) = '1') then
			next_state <= CASE_1;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
   -- - - - - - - - - - - - - - - - - - - - - - -
   when CASE_1 =>
      next_state <= CASE_1;
		if (KEY(5) = '1') then
			next_state <= CASE_5;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	when CASE_5 =>
		next_state <= CASE_5;
		if (KEY(3) = '1') then
			next_state <= CASE_3;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	when CASE_3 =>
		next_state <= CASE_3;
		if (KEY(4) = '1') then
			next_state <= CASE1_4;
		elsif (KEY(7) = '1') then
			next_state <= CASE2_7;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	when CASE1_4 =>
		next_state <= CASE1_4;
		if (KEY(8) = '1') then
			next_state <= CASE1_81;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
   when CASE1_81 =>
		next_state <= CASE1_81;
		if (KEY(8) = '1') then
			next_state <= CASE1_82;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	when CASE1_82 =>
		next_state <= CASE1_82;
		if (KEY(6) = '1') then
			next_state <= CASE1_6;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - - 
   when CASE1_6 =>
		next_state <= CASE1_6;
		if (KEY(5) = '1') then
			next_state <= CASE1_5;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	when CASE1_5 =>
		next_state <= CASE1_5;
		if (KEY(0) = '1') then
			next_state <= CASE1_0;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	when CASE1_0 =>
		next_state <= CASE1_0;
		if (KEY(3) = '1') then
			next_state <= CASE_CORRECT;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -

	when CASE2_7 =>
		next_state <= CASE2_7;
		if (KEY(9) = '1') then
			next_state <= CASE2_9;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	when CASE2_9 =>
		next_state <= CASE2_9;
		if (KEY(2) = '1') then
			next_state <= CASE2_21;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	
	when CASE2_21 =>
		next_state <= CASE2_21;
		if (KEY(0) = '1') then
			next_state <= CASE2_0;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	
	when CASE2_0 =>
		next_state <= CASE2_0;
		if (KEY(2) = '1') then
			next_state <= CASE2_22;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	when CASE2_22 =>
		next_state <= CASE2_22;
		if (KEY(2) = '1') then
			next_state <= CASE2_23;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	when CASE2_23 =>
		next_state <= CASE2_23;
		if (KEY(6) = '1') then
			next_state <= CASE_CORRECT;
      elsif (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	
	 when CASE_CORRECT =>
		next_state <= CASE_CORRECT;
      if (KEY(15) = '1') then
         next_state <= PRINT_CORRECT; 
		elsif (KEY(14 downto 0) /= "000000000000000") then
			next_state <= CASE_ERROR;
      end if;
	-- - - - - - - - - - - - - - - - - - - - - - -
	
	 when CASE_ERROR =>
		next_state <= CASE_ERROR;
      if (KEY(15) = '1') then
         next_state <= PRINT_ERROR; 
      end if;
   -- - - - - - - - - - - - - - - - - - - - - - -
   when PRINT_CORRECT =>
		next_state <= PRINT_CORRECT;
      if (CNT_OF = '1') then
         next_state <= FINISH;
      end if;
   -- - - - - - - - - - - - - - - - - - - - - - -
   when PRINT_ERROR =>
      next_state <= PRINT_ERROR;
      if (CNT_OF = '1') then
         next_state <= FINISH;
      end if;
   -- - - - - - - - - - - - - - - - - - - - - - -
   when FINISH =>
      next_state <= FINISH;
      if (KEY(15) = '1') then
         next_state <= DEFAULT; 
      end if;
   -- - - - - - - - - - - - - - - - - - - - - - -
   when others =>
      next_state <= DEFAULT;
   end case;
end process next_state_logic;

-- -------------------------------------------------------
output_logic : process(present_state, KEY)
begin
   FSM_CNT_CE     <= '0';
   FSM_MX_MEM     <= '0';
   FSM_MX_LCD     <= '0';
   FSM_LCD_WR     <= '0';
   FSM_LCD_CLR    <= '0';

   case (present_state) is
   -- - - - - - - - - - - - - - - - - - - - - - -
   when DEFAULT | CASE_ERROR | CASE_CORRECT |CASE_1 | CASE_5 | CASE_3 | CASE1_4 | CASE1_81 | CASE1_82 | CASE1_6 | CASE1_5 |CASE1_0 | CASE2_7 | CASE2_9 | CASE2_21 | CASE2_0 | CASE2_22 | CASE2_23  =>
      if (KEY(14 downto 0) /= "000000000000000") then
         FSM_LCD_WR     <= '1';
      end if;
      if (KEY(15) = '1') then
         FSM_LCD_CLR    <= '1';
      end if;
   -- - - - - - - - - - - - - - - - - - - - - - -
   when PRINT_ERROR =>
      FSM_CNT_CE     <= '1';
      FSM_MX_LCD     <= '1';
      FSM_LCD_WR     <= '1';
   -- - - - - - - - - - - - - - - - - - - - - - -
	   when PRINT_CORRECT =>
      FSM_CNT_CE     <= '1';
      FSM_MX_LCD     <= '1';
      FSM_LCD_WR     <= '1';
		FSM_MX_MEM     <= '1';
   -- - - - - - - - - - - - - - - - - - - - - - -
	
   when FINISH =>
      if (KEY(15) = '1') then
         FSM_LCD_CLR    <= '1';
      end if;
   -- - - - - - - - - - - - - - - - - - - - - - -
   when others =>
   end case;
end process output_logic;

end architecture behavioral;

