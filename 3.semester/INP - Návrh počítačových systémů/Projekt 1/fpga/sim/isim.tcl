proc isim_script {} {

   add_divider "Signals of the Vigenere Interface"
   add_wave_label "" "CLK" /testbench/clk
   add_wave_label "" "RST" /testbench/rst
   add_wave_label "-radix ascii" "DATA" /testbench/tb_data
   add_wave_label "-radix ascii" "KEY" /testbench/tb_key
   add_wave_label "-radix ascii" "CODE" /testbench/tb_code

   add_divider "Vigenere Inner Signals"
   add_wave_label "-radix hexadecimal" "state" /testbench/uut/state
   # sem doplnte vase vnitrni signaly. chcete-li v diagramu zobrazit desitkove
   # cislo, vlozte do prvnich uvozovek: -radix dec

   add_wave_label "-radix ascii" "SHIFT" /testbench/uut/shiftSignal
   add_wave_label "-radix ascii" "PLUS" /testbench/uut/plusSignal
   add_wave_label "-radix ascii" "MINUS" /testbench/uut/minusSignal


   run 8 ns
}

