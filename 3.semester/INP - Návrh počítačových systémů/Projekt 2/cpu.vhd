-- cpu.vhd: Simple 8-bit CPU (BrainF*ck interpreter)
-- Copyright (C) 2020 Brno University of Technology,
--                    Faculty of Information Technology
-- Author(s): Vanesa Jóriová - xjorio00
--

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;

-- ----------------------------------------------------------------------------
--                        Entity declaration
-- ----------------------------------------------------------------------------
entity cpu is
 port (
   CLK   : in std_logic;  -- hodinovy signal
   RESET : in std_logic;  -- asynchronni reset procesoru
   EN    : in std_logic;  -- povoleni cinnosti procesoru
 
   -- synchronni pamet ROM
   CODE_ADDR : out std_logic_vector(11 downto 0); -- adresa do pameti
   CODE_DATA : in std_logic_vector(7 downto 0);   -- CODE_DATA <- rom[CODE_ADDR] pokud CODE_EN='1'
   CODE_EN   : out std_logic;                     -- povoleni cinnosti
   
   -- synchronni pamet RAM
   DATA_ADDR  : out std_logic_vector(9 downto 0); -- adresa do pameti
   DATA_WDATA : out std_logic_vector(7 downto 0); -- ram[DATA_ADDR] <- DATA_WDATA pokud DATA_EN='1'
   DATA_RDATA : in std_logic_vector(7 downto 0);  -- DATA_RDATA <- ram[DATA_ADDR] pokud DATA_EN='1'
   DATA_WE    : out std_logic;                    -- cteni (0) / zapis (1)
   DATA_EN    : out std_logic;                    -- povoleni cinnosti 
   
   -- vstupni port
   IN_DATA   : in std_logic_vector(7 downto 0);   -- IN_DATA <- stav klavesnice pokud IN_VLD='1' a IN_REQ='1'
   IN_VLD    : in std_logic;                      -- data platna
   IN_REQ    : out std_logic;                     -- pozadavek na vstup data
   
   -- vystupni port
   OUT_DATA : out  std_logic_vector(7 downto 0);  -- zapisovana data
   OUT_BUSY : in std_logic;                       -- LCD je zaneprazdnen (1), nelze zapisovat
   OUT_WE   : out std_logic                       -- LCD <- OUT_DATA pokud OUT_WE='1' a OUT_BUSY='0'
 );
end cpu;


-- ----------------------------------------------------------------------------
--                      Architecture declaration
-- ----------------------------------------------------------------------------
architecture behavioral of cpu is

 --- Programovy citac
	signal pc : std_logic_vector (11 downto 0);
	signal pc_inc : std_logic; --inkrementacia
	signal pc_dec : std_logic; --dekrementacia
	signal pc_ld : std_logic;  --load
	signal pc_zero : std_logic;

 ---- RAS
	signal ras : std_logic_vector (11 downto 0); 
	
 ---- PTR
	signal ptr : std_logic_vector (9 downto 0);
	signal ptr_inc : std_logic;
	signal ptr_dec : std_logic;
	signal ptr_zero : std_logic;

 --- Multiplexor	
	signal mx_data_out: std_logic_vector (7 downto 0);
	signal mx_data_select: std_logic_vector (1 downto 0);

	
 ---- FSM Mealy States

	type fsm_state is (

		state_idle, 
		state_fetch,
		state_decode, 

		state_ptr_inc, 
		state_ptr_dec, 
		
		state_cell_inc,
		state_cell_inc_2,
		state_cell_inc_3,

		state_cell_dec, 
		state_cell_dec_2,
		state_cell_dec_3,
		
		state_while_bracket,
		state_while_bracket_2, 
		state_while_bracket_3,
		state_while_bracket_4,


		state_while_end, 
		
		state_print,
	   state_print_2,
	
		state_load,
		state_load_2,

		state_null,
		state_unknown
	);	


	signal pstate: fsm_state := state_idle;
        signal nstate: fsm_state;

	

begin

	multiplexor: process (mx_data_select, CLK, RESET) is
	begin
		if RESET = '1' then
			mx_data_out  <= (others => '0');
		elsif (CLK'event) and (CLK='1') then 
			if (mx_data_select = "00") then
      				mx_data_out <= IN_DATA;
   			elsif (mx_data_select = "01") then
      				mx_data_out <= DATA_RDATA + 1;
   			elsif (mx_data_select = "10") then
      				mx_data_out <= DATA_RDATA - 1;
   			else
      				mx_data_out <=  (others => '0');
   			end if;
			
		
		end if;
	end process;


	DATA_WDATA <= mx_data_out;
	
	OUT_DATA <= DATA_RDATA; --zapis

	
	pc_process: process (pc_inc, pc_dec, pc_ld, CLK, RESET) is
	begin

		if (RESET = '1') then
		pc  <= (others => '0');
		elsif (CLK'event) and (CLK='1') then 
			if (pc_inc = '1') then
				pc <= pc + 1;
			elsif (pc_dec = '1') then
				pc <= pc - 1;
			elsif (pc_ld = '1') then
				pc <= ras;
			elsif (pc_zero = '1') then
				pc <= (others => '0');
			end if;
			
		end if;
	end process;
	CODE_ADDR <= pc;


	ptr_proces: process (ptr_inc, ptr_dec, CLK, RESET) is 
	begin
		
		if (RESET = '1') then
		ptr  <= (others => '0');
		elsif (CLK'event) and (CLK='1') then 
			if (ptr_inc = '1') then
				ptr <= ptr + 1;
			elsif (ptr_dec = '1') then
				ptr <= ptr - 1;
			elsif (ptr_zero = '1') then
				ptr <= (others => '0');
			end if;
			
		end if;	
	end process;
	DATA_ADDR <= ptr;


	fsm_state_process: process (EN, CLK, RESET) is
	begin
		if (RESET = '1') then
			pstate  <= state_idle;
		elsif (CLK'event) and (CLK='1') then 
			if (EN = '1') then
				pstate  <= nstate;
			end if;
		end if;
	end process;

	fsm_nstate_process: process(pstate, CODE_DATA, DATA_RDATA, IN_VLD, OUT_BUSY) is
	begin


		DATA_EN <= '0';
		DATA_WE <= '0';
		CODE_EN <= '0';
		IN_REQ <= '0';
		OUT_WE <= '0';
		pc_inc <= '0';
		pc_dec <= '0';
		pc_ld <= '0';
		pc_zero <= '0';
		ptr_zero <= '0';
		ptr_inc <= '0';
		ptr_dec <= '0';

		mx_data_select <= "00";

		case pstate is
		       when state_idle =>
			       pc_zero <= '1';
			       ptr_zero <= '1';
			       nstate <= state_fetch;
			when state_fetch =>
				CODE_EN <= '1';
				nstate <= state_decode;
			when state_decode =>
				case CODE_DATA is
					when  X"3E" =>
						nstate <= state_ptr_inc;

					when  X"3C" => 
						nstate <= state_ptr_dec;

					when X"2B" => 
						nstate <= state_cell_inc;

					when X"2D" => 
						nstate <= state_cell_dec;

					when X"5B" => 
						nstate <= state_while_bracket;
					when X"5D" => 
						nstate <= state_while_end;
					when X"2E" => 
						nstate <= state_print;
					when X"2C" => 
						nstate <= state_load;
					when X"00" => 
						nstate <= state_null;

					when others => 
						nstate <= state_unknown;
				end case;

			when state_ptr_inc => 
				pc_inc <= '1';
				ptr_inc <= '1';
				nstate <= state_fetch;

			when state_ptr_dec => 
				pc_inc <= '1';
				ptr_dec <= '1';
				nstate <= state_fetch;


			---- + 0x2B -----

			when state_cell_inc => 
				DATA_EN <= '1';
				DATA_WE <= '0';
				nstate <= state_cell_inc_2;

			when state_cell_inc_2 => 
				mx_data_select <= "01";
				nstate <= state_cell_inc_3;

			when state_cell_inc_3 => 
				pc_inc <= '1';
				DATA_EN <= '1';
				DATA_WE <= '1';
				nstate <= state_fetch;


			---- - 0x2D -----

			when state_cell_dec => 
				DATA_EN <= '1';
				DATA_WE <= '0';
				nstate <= state_cell_dec_2;

			when state_cell_dec_2 => 
				mx_data_select <= "10";
				nstate <= state_cell_dec_3;

			when state_cell_dec_3 => 
				pc_inc <= '1';
				DATA_EN <= '1';
				DATA_WE <= '1';
				nstate <= state_fetch;



			---- [ 0x5B -----
			when state_while_bracket =>
				pc_inc <= '1';
				DATA_EN <= '1';
				DATA_WE <= '0';
				ras <= pc;
				nstate <= state_while_bracket_2;
				
			when state_while_bracket_2 =>
				if (DATA_RDATA = "00000000") then
					DATA_EN <= '1';
					nstate <= state_while_bracket_3;	
				else 
					nstate <= state_fetch;
				end if;


			-- while loop	
			when state_while_bracket_3 => 
				pc_inc <= '1';
				if CODE_DATA = X"5D" then
					nstate <= state_fetch;	
				else 
					nstate <= state_while_bracket_4;
				end if;


			-- data enable
			when state_while_bracket_4 => 
				DATA_EN <= '1';
				nstate <= state_while_bracket_3;



			---- ] 0x5D -----
			when state_while_end =>
				if (DATA_RDATA = "00000000") then
					pc_inc <= '1';
				        nstate <= state_fetch;	
				
				else 
					
					pc_ld <= '1';
					nstate <= state_fetch;	
				
				end if;

			---- . 0x2E -----

			when state_print =>
				DATA_EN <= '1';
				DATA_WE <= '0';
				nstate <= state_print_2;

			when state_print_2 =>
				if OUT_BUSY = '1' then
					DATA_EN <= '1';
					DATA_WE <= '0';
					nstate <= state_print_2;
				else 
					OUT_WE <= '1';
					pc_inc <= '1';
					nstate <= state_fetch;
					

				end if; 

			
			
			
			---- , 0x2C -----

			when state_load =>
				IN_REQ <= '1';
				mx_data_select <= "00";
				nstate <= state_load_2;

			when state_load_2 =>
				if IN_VLD /= '1' then
					IN_REQ <= '1';
					mx_data_select <= "00";
					nstate <= state_load_2;
				else 
					pc_inc <= '1';
					DATA_EN <= '1';
					DATA_WE <= '1';
					nstate <= state_fetch;
					

				end if;	



			when state_null =>
				nstate <= state_null;


			when state_unknown =>
				pc_inc <= '1';
				nstate <= state_fetch;


			end case;

	end process;






 
end behavioral;
 

