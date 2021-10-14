#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include "lcd.h"
//char str[50];
void convert(int n){
    if(n<=0){
        //str[i] = '\0';
        return;
    }
    else{
        convert(n/2);
        LCD_Char(n%2 + '0');
        //printf("%d", n%2);
    }
}


int main(void){

    DDRB = 0xFF; // 1111.1111; set PB0-PB7 as outputs
    LCD_Init(); // Initializing LCD controller
    LCD_Clear();
    convert(45);
    //_delay_ms(1000);
    //LCD_Clear();
	return 0;
}
