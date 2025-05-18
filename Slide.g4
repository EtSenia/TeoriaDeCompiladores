
grammar Slide;

prog: stat* EOF
    ;

stat: expr ';'
    ;


expr: slide
    ;

slide    : 'Slide' ID '{' (text | img | bg)* '}';
text    : 'Text'  '{' ((transform | text_prop) ';')* '}';
img     : 'Image' '{' ((transform | src) ';')* '}';


transform   : position
            | width
            | height
            ;

text_prop   : textCont
            | fontSize
            | fontFam
            | align
            ;

src         : 'src=' STR;
bg          : 'bg=' STR;

position    : 'position=' UNIDAD ',' UNIDAD;
rotation    : 'rotation=' INT;
width       : 'width='  UNIDAD;
height      : 'height='  UNIDAD;

textCont    : 'content=' STR;
fontSize    : 'font-size=' INT;
fontFam     : 'font-family=' STR;
align       : 'align=' ALIGN;

ALIGN: 'center'
    |  'left'
    |  'right'
    |  'justified';

UNIDAD: INT+ ('%' | 'px') ;

INT : [0-9]+ ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
STR : '"' (~[\r\n])* '"' ;
TEXT_BLOCK : '"""' .*? '"""' -> type(STR);
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

WS  : [ \t\r\n]+ -> skip;
