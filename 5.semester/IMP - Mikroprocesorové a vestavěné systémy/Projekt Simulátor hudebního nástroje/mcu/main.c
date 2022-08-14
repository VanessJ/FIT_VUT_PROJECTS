#include <fitkitlib.h>
#include <keyboard/keyboard.h>
#include <lcd/display.h>
#include <ctype.h>
#include <string.h>

// znaky vo formate ton-oktava, bez specifikacie oktavy sa jedna o stvrtu oktavu
#define C 262
#define D 294
#define E 329
#define F 349
#define G 392
#define A 440
#define B 493
#define A3 220
#define B3 247
#define D5 587

#define TEMPO 6 //znizenie pre zruchlenie demo skladieb, zvysenie hodnoty pre spomalenie

// prevzate z https://create.arduino.cc/projecthub/akkuadlakha5/play-songs-using-arduino-0d90ed
int CrazyFrog_note[] = {
    D, 0, F, D, 0, D, G, D, C,
    D, 0, A, D, 0, D, A, A, F,
    D, A, D5, D, C, 0, C, A3, E, D,
    0, D, D};
int CrazyFrog_duration[] = {
    8, 8, 6, 16, 16, 16, 8, 8, 8,
    8, 8, 6, 16, 16, 16, 8, 8, 8,
    8, 8, 8, 16, 16, 16, 16, 8, 8, 2,
    8, 4, 4};

// prevzate z https://create.arduino.cc/projecthub/akkuadlakha5/play-songs-using-arduino-0d90ed
int Pirates_note[] = {
    D, D, D, D, D, D, D, D,
    D, D, D, D, D, D, D, D,
    D, D, D, D, D, D, D, D,
    A3, C, D, D, D, E, F, F,
    F, G, E, E, D, C, C, D,
    0, A3, C, B3, D, B3, E, F,
    F, C, C, C, C, D, C,
    D, 0, 0, A3, C, D, D, D, F,
    G, G, G, A, A, A, A, G,
    A, D, 0, D, E, F, F, G, A,
    D, 0, D, F, E, E, F, D};
int Pirates_duration[] = {
    4, 8, 4, 8, 4, 8, 8, 8, 8, 4, 8, 4, 8, 4, 8, 8, 8, 8, 4, 8, 4, 8,
    4, 8, 8, 8, 8, 4, 4, 8, 8, 4, 4, 8, 8, 4, 4, 8, 8,
    8, 4, 8, 8, 8, 4, 4, 8, 8, 4, 4, 8, 8, 4, 4, 8, 4,
    4, 8, 8, 8, 8, 4, 4, 8, 8, 4, 4, 8, 8, 4, 4, 8, 8,
    8, 4, 8, 8, 8, 4, 4, 4, 8, 4, 8, 8, 8, 4, 4, 8, 8};

// zvuk je prehravany
#define SOUND_ON 1

// vypnutie zvuku
#define SOUND_OFF 0

#define HIGH 255
#define LOW 0

// v case prehravania sa nastavi na SOUND_ON, po pozadovanej dlzke znenia prenastavi na sound_off
int playing = SOUND_OFF;

// pri generacii obdlznikoveho signalu sa striedaju amplitudy HIGH (255) a LOW(0)
int sample = LOW;

// pocet tikov za sekundu
#define CLOCK_TICK_SECOND 32768 // 0x8000 Hz

// pocet vzoriek obdlznikoveho signalu
#define SQUARE_SAMPLES 2

// Pocet tikov, po ktorych dojde k nasledujucemu preruseniu (zavisi od frekvencie)
int tone = A;
int ticks;

void print_user_help(void);
void fpga_initialized();
unsigned char decode_user_cmd(char *UserCommand, char *ComparedCommand);
int keyboard_idle();
void play_note(int note, int duration_divide);
void play_pirates();
void play_crazy_frog();

int main(void)
{
    ticks = CLOCK_TICK_SECOND / tone / SQUARE_SAMPLES;
    initialize_hardware();
    WDG_stop();

    // Casovac
    CCTL0 = CCIE;
    CCR0 = ticks;
    TACTL = TASSEL_1 + MC_2;

    // AD a DA prevodnik

    ADC12CTL0 |= 0x0020;
    DAC12_0CTL |= 0x1060;
    DAC12_0CTL |= 0x100;

    while (1)
    {
        keyboard_idle(); // obsluha klavesnice
        terminal_idle(); // obsluha terminalu
    }
}

void play_pirates()
{
    int i;
    int delay;
    for (i = 0; i < 88; i++)
    {
        if (Pirates_note[i] == 0)
        {
            delay = 1000 / Pirates_duration[i];
            delay_ms(delay);
        }
        else
        {
            play_note(Pirates_note[i], Pirates_duration[i]);
        }
        int note_duration = Pirates_duration[i] * TEMPO;
        delay_ms(note_duration);
    }
}

void play_crazy_frog()
{
    int delay;
    int i;
    for (i = 0; i < 31; i++)
    {
        if (CrazyFrog_note[i] == 0)
        {
            delay = 1000 / CrazyFrog_duration[i];
            delay_ms(delay);
        }
        else
        {
            play_note(CrazyFrog_note[i], CrazyFrog_duration[i]);
        }
        int note_duration = CrazyFrog_duration[i] * TEMPO;
        delay_ms(note_duration);
    }
}

interrupt(TIMERA0_VECTOR) Timer_A(void)
{

    /**
     * aby ton "znel" ako ton, je nutne striedat urovne 0 a 255 obdlznikoveho signalu.
     * K tomu dochadza po urcitom pocte tikov v zavislosti od frekvencie daneho tonu.
     *
     */

    if (sample == HIGH)
    {
        sample = LOW;
    }

    else if (sample == LOW)
    {
        sample = HIGH;
    }

    DAC12_0DAT = sample * playing; // dalsia vzorka na prevod
    CCR0 += ticks;                 // pocet tikov, po ktorom prejde k dalsiemu preruseniu
}

void fpga_initialized()
{
    LCD_init();
    LCD_write_string("Simulator hudobneho nastroja");
    term_send_str_crlf("Pripojte svoj reproduktor na pin 31 JP9 a na GND");
    term_send_str_crlf("Popis ovladania sa zobrazi po napisani help do terminalu");
}

// obsluha klavesnice a stlacenia jednotlivych znakov
int keyboard_idle()
{
    char ch;
    ch = key_decode(read_word_keyboard_4x4());
    if (ch != 0)
    {
        switch (ch)
        {
        case '1':
            LCD_clear();
            LCD_append_string("Nota A");
            term_send_str_crlf("Prehrava sa nota A");
            play_note(A, 4);
            break;
        case '2':
            LCD_clear();
            LCD_append_string("Nota B");
            term_send_str_crlf("Prehrava sa nota B");
            play_note(B, 4);
            break;

        case '3':
            LCD_clear();
            LCD_append_string("Nota C");
            term_send_str_crlf("Prehrava sa nota C");
            play_note(C, 4);
            break;

        case '4':
            LCD_clear();
            LCD_append_string("Nota D");
            term_send_str_crlf("Prehrava sa nota D");
            play_note(D, 4);
            break;
        case '5':
            LCD_clear();
            LCD_append_string("Nota E");
            term_send_str_crlf("Prehrava sa nota E");
            play_note(E, 4);
            break;
        case '6':
            LCD_clear();
            LCD_append_string("Nota F");
            term_send_str_crlf("Prehrava sa nota F");
            play_note(F, 4);
            break;
        case '7':
            LCD_clear();
            LCD_append_string("Nota G");
            term_send_str_crlf("Prehrava sa nota G");
            play_note(G, 4);
            break;

        case '8':
            LCD_clear();
            LCD_append_string("HE'S A PIRATE demo");
            term_send_str_crlf("Prehrava sa demo melodia");
            play_pirates();
            break;

        case '9':
            LCD_clear();
            LCD_append_string("Crazy frog demo");
            term_send_str_crlf("Prehrava sa demo melodia");
            play_crazy_frog();
            break;
        }
    }
}


void print_user_help(void)
{
    term_send_str_crlf("Ovladanie simulatora je mozne pomocou klavesnice alebo terminalu.");
    term_send_str_crlf("Klavesy 1-7 prisluchaju tonom A-G (v presnom poradi).");
    term_send_str_crlf("Klavesa 8 prehra predpripravenu melodiu - He's a pirate.");
    term_send_str_crlf("Klavesa 9 prehra predpripravenu melodiu - Crazy Frog.");
    term_send_str_crlf("Po zadani znakov A-G do terminalu sa prehra zadana melodia.");
    term_send_str_crlf("Znaky A-G prisluchaju prislusnemu tonu, medzera pauze 300ms medzi tonmi.");
    term_send_str_crlf("Nepodporovane znaky automaticky vedu na pauzu medzi tonmi.");
}


//obsluha terminalu
unsigned char decode_user_cmd(char *cmd_ucase, char *cmd)
{
    int len = strlen(cmd_ucase);
    int i;
    for (i = 0; i < len; i++)
    {
        char c = toupper(cmd_ucase[i]);
        switch (c)
        {
        case 'A':
            play_note(A, 4);
            break;
        case 'B':
            play_note(B, 4);
            break;
        case 'C':
            play_note(C, 4);
            break;
        case 'D':
            play_note(D, 4);
            break;
        case 'E':
            play_note(E, 4);
            break;
        case 'F':
            play_note(F, 4);
            break;
        case 'G':
            play_note(G, 4);
            break;
        case ' ':
            delay_ms(250);
            break;
        default:
            delay_ms(250);
            break;
        }
    }
    return USER_COMMAND;
}

void play_note(int note, int duration_divide)
{
    int tone = note;
    ticks = CLOCK_TICK_SECOND / tone / SQUARE_SAMPLES;
    playing = SOUND_ON; // zapnutie hlasitosti a zahratie dekodovaneho tonu z klavesnice
    delay_ms(1000 / duration_divide);
    playing = SOUND_OFF;
}
