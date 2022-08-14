library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_arith.all;
use IEEE.std_logic_unsigned.all;

-- rozhrani Vigenerovy sifry
entity vigenere is
   port(
         CLK : in std_logic;
         RST : in std_logic;
         DATA : in std_logic_vector(7 downto 0);
         KEY : in std_logic_vector(7 downto 0);

         CODE : out std_logic_vector(7 downto 0)
    );
end vigenere;

-- V souboru fpga/sim/tb.vhd naleznete testbench, do ktereho si doplnte
-- znaky vaseho loginu (velkymi pismeny) a znaky klice dle vaseho prijmeni.

architecture behavioral of vigenere is

	signal shiftSignal: std_logic_vector(7 downto 0);
	signal plusSignal: std_logic_vector(7 downto 0);
	signal minusSignal: std_logic_vector(7 downto 0);

	type tState is (plusState, minusState);
	signal state: tState := plusState;
	signal nextState: tState := minusState;

	signal MealySignal: std_logic_vector(1 downto 0);



begin


	psatereg: process (CLK, RST) is
	begin
		if RST = '1' then
			state <= plusState;
		elsif (CLK'event) and (CLK='1') then
		      state <= nextState;
		end if;
  	end process;
	
	
	nstate_logic: process (RST, DATA, state) is
	begin
		case state is
			when plusState =>
				MealySignal <= "00";
				nextState <= minusState; 
			when minusState =>
				MealySignal <= "01";
				nextState <= PlusState;
		end case;


		
		if (DATA > 47 and DATA < 58) then
			MealySignal <= "11";
		end if;

		
		if RST = '1'
		then 
			MealySignal <= "10";
		end if;

				
	end process;


	
	
	CODE <= PlusSignal when (MealySignal = "00") else
		MinusSignal when (MealySignal = "01") else
		"00100011";
			









	newCharProcess: process (KEY, DATA) is
	begin
		shiftSignal <= KEY - 64;

	end process;

	
	
	plusCorrection: process (DATA, shiftSignal) is
	
		variable temp: std_logic_vector(7 downto 0);
		variable correction:  std_logic_vector(7 downto 0);
	
	begin
		temp := DATA + shiftSignal; 
		
		if (temp > 90) then
			correction := temp - 90;
		       temp := 64 + correction;
	       end if;
		plusSignal <= temp;	       

	end process;

	

	
	minusCorrection: process (DATA, shiftSignal) is
	
		variable temp: std_logic_vector(7 downto 0);
		variable correction:  std_logic_vector(7 downto 0);
	
	begin
		temp := DATA - shiftSignal; 
		
		if (temp < 65) then
			correction := 64 - temp;
		        temp := 90 - correction;	
	       end if;
		minusSignal <= temp;	       

	end process; 


	




    -- Sem doplnte popis obvodu. Doporuceni: pouzivejte zakladni obvodove prvky
    -- (multiplexory, registry, dekodery,...), jejich funkce popisujte pomoci
    -- procesu VHDL a propojeni techto prvku, tj. komunikaci mezi procesy,
    -- realizujte pomoci vnitrnich signalu deklarovanych vyse.

    -- DODRZUJTE ZASADY PSANI SYNTETIZOVATELNEHO VHDL KODU OBVODOVYCH PRVKU,
    -- JEZ JSOU PROBIRANY ZEJMENA NA UVODNICH CVICENI INP A SHRNUTY NA WEBU:
    -- http://merlin.fit.vutbr.cz/FITkit/docs/navody/synth_templates.html.


end behavioral;


