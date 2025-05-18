# Generated from Slide.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,51,8,3,10,3,12,3,54,9,3,
        1,3,1,3,1,4,1,4,1,4,1,4,5,4,62,8,4,10,4,12,4,65,9,4,1,4,1,4,1,5,
        1,5,1,5,1,5,5,5,73,8,5,10,5,12,5,76,9,5,1,5,1,5,1,6,1,6,1,6,3,6,
        83,8,6,1,7,1,7,1,7,1,7,3,7,89,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,
        1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,0,120,0,
        35,1,0,0,0,2,40,1,0,0,0,4,43,1,0,0,0,6,45,1,0,0,0,8,57,1,0,0,0,10,
        68,1,0,0,0,12,82,1,0,0,0,14,88,1,0,0,0,16,90,1,0,0,0,18,94,1,0,0,
        0,20,100,1,0,0,0,22,104,1,0,0,0,24,108,1,0,0,0,26,112,1,0,0,0,28,
        116,1,0,0,0,30,120,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,1,0,
        0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,
        5,0,0,1,39,1,1,0,0,0,40,41,3,4,2,0,41,42,5,1,0,0,42,3,1,0,0,0,43,
        44,3,6,3,0,44,5,1,0,0,0,45,46,5,2,0,0,46,47,5,19,0,0,47,52,5,3,0,
        0,48,51,3,8,4,0,49,51,3,10,5,0,50,48,1,0,0,0,50,49,1,0,0,0,51,54,
        1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,
        55,56,5,4,0,0,56,7,1,0,0,0,57,58,5,5,0,0,58,63,5,3,0,0,59,62,3,12,
        6,0,60,62,3,14,7,0,61,59,1,0,0,0,61,60,1,0,0,0,62,65,1,0,0,0,63,
        61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,4,0,
        0,67,9,1,0,0,0,68,69,5,6,0,0,69,74,5,3,0,0,70,73,3,12,6,0,71,73,
        3,16,8,0,72,70,1,0,0,0,72,71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,
        74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,78,5,4,0,0,78,11,1,
        0,0,0,79,83,3,18,9,0,80,83,3,20,10,0,81,83,3,22,11,0,82,79,1,0,0,
        0,82,80,1,0,0,0,82,81,1,0,0,0,83,13,1,0,0,0,84,89,3,24,12,0,85,89,
        3,26,13,0,86,89,3,28,14,0,87,89,3,30,15,0,88,84,1,0,0,0,88,85,1,
        0,0,0,88,86,1,0,0,0,88,87,1,0,0,0,89,15,1,0,0,0,90,91,5,7,0,0,91,
        92,5,20,0,0,92,93,5,1,0,0,93,17,1,0,0,0,94,95,5,8,0,0,95,96,5,17,
        0,0,96,97,5,9,0,0,97,98,5,17,0,0,98,99,5,1,0,0,99,19,1,0,0,0,100,
        101,5,10,0,0,101,102,5,17,0,0,102,103,5,1,0,0,103,21,1,0,0,0,104,
        105,5,11,0,0,105,106,5,17,0,0,106,107,5,1,0,0,107,23,1,0,0,0,108,
        109,5,12,0,0,109,110,5,20,0,0,110,111,5,1,0,0,111,25,1,0,0,0,112,
        113,5,13,0,0,113,114,5,18,0,0,114,115,5,1,0,0,115,27,1,0,0,0,116,
        117,5,14,0,0,117,118,5,20,0,0,118,119,5,1,0,0,119,29,1,0,0,0,120,
        121,5,15,0,0,121,122,5,16,0,0,122,123,5,1,0,0,123,31,1,0,0,0,9,35,
        50,52,61,63,72,74,82,88
    ]

class SlideParser ( Parser ):

    grammarFileName = "Slide.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'Slide'", "'{'", "'}'", "'Text'", 
                     "'Image'", "'src='", "'position='", "','", "'width='", 
                     "'height='", "'content='", "'font-size='", "'font-family='", 
                     "'align='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ALIGN", "UNIDAD", "INT", "ID", "STR", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_slide = 3
    RULE_text = 4
    RULE_img = 5
    RULE_transform = 6
    RULE_text_prop = 7
    RULE_src = 8
    RULE_position = 9
    RULE_width = 10
    RULE_height = 11
    RULE_textCont = 12
    RULE_fontSize = 13
    RULE_fontFam = 14
    RULE_align = 15

    ruleNames =  [ "prog", "stat", "expr", "slide", "text", "img", "transform", 
                   "text_prop", "src", "position", "width", "height", "textCont", 
                   "fontSize", "fontFam", "align" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    ALIGN=16
    UNIDAD=17
    INT=18
    ID=19
    STR=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SlideParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlideParser.StatContext)
            else:
                return self.getTypedRuleContext(SlideParser.StatContext,i)


        def getRuleIndex(self):
            return SlideParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = SlideParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 32
                self.stat()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(SlideParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SlideParser.ExprContext,0)


        def getRuleIndex(self):
            return SlideParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = SlideParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.expr()
            self.state = 41
            self.match(SlideParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def slide(self):
            return self.getTypedRuleContext(SlideParser.SlideContext,0)


        def getRuleIndex(self):
            return SlideParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = SlideParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.slide()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SlideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SlideParser.ID, 0)

        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlideParser.TextContext)
            else:
                return self.getTypedRuleContext(SlideParser.TextContext,i)


        def img(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlideParser.ImgContext)
            else:
                return self.getTypedRuleContext(SlideParser.ImgContext,i)


        def getRuleIndex(self):
            return SlideParser.RULE_slide

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSlide" ):
                listener.enterSlide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSlide" ):
                listener.exitSlide(self)




    def slide(self):

        localctx = SlideParser.SlideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_slide)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(SlideParser.T__1)
            self.state = 46
            self.match(SlideParser.ID)
            self.state = 47
            self.match(SlideParser.T__2)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 50
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5]:
                    self.state = 48
                    self.text()
                    pass
                elif token in [6]:
                    self.state = 49
                    self.img()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(SlideParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def transform(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlideParser.TransformContext)
            else:
                return self.getTypedRuleContext(SlideParser.TransformContext,i)


        def text_prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlideParser.Text_propContext)
            else:
                return self.getTypedRuleContext(SlideParser.Text_propContext,i)


        def getRuleIndex(self):
            return SlideParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)




    def text(self):

        localctx = SlideParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(SlideParser.T__4)
            self.state = 58
            self.match(SlideParser.T__2)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 64768) != 0):
                self.state = 61
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 10, 11]:
                    self.state = 59
                    self.transform()
                    pass
                elif token in [12, 13, 14, 15]:
                    self.state = 60
                    self.text_prop()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(SlideParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def transform(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlideParser.TransformContext)
            else:
                return self.getTypedRuleContext(SlideParser.TransformContext,i)


        def src(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlideParser.SrcContext)
            else:
                return self.getTypedRuleContext(SlideParser.SrcContext,i)


        def getRuleIndex(self):
            return SlideParser.RULE_img

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImg" ):
                listener.enterImg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImg" ):
                listener.exitImg(self)




    def img(self):

        localctx = SlideParser.ImgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_img)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(SlideParser.T__5)
            self.state = 69
            self.match(SlideParser.T__2)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3456) != 0):
                self.state = 72
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 10, 11]:
                    self.state = 70
                    self.transform()
                    pass
                elif token in [7]:
                    self.state = 71
                    self.src()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.match(SlideParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransformContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def position(self):
            return self.getTypedRuleContext(SlideParser.PositionContext,0)


        def width(self):
            return self.getTypedRuleContext(SlideParser.WidthContext,0)


        def height(self):
            return self.getTypedRuleContext(SlideParser.HeightContext,0)


        def getRuleIndex(self):
            return SlideParser.RULE_transform

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransform" ):
                listener.enterTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransform" ):
                listener.exitTransform(self)




    def transform(self):

        localctx = SlideParser.TransformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_transform)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.position()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.width()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.height()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Text_propContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def textCont(self):
            return self.getTypedRuleContext(SlideParser.TextContContext,0)


        def fontSize(self):
            return self.getTypedRuleContext(SlideParser.FontSizeContext,0)


        def fontFam(self):
            return self.getTypedRuleContext(SlideParser.FontFamContext,0)


        def align(self):
            return self.getTypedRuleContext(SlideParser.AlignContext,0)


        def getRuleIndex(self):
            return SlideParser.RULE_text_prop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText_prop" ):
                listener.enterText_prop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText_prop" ):
                listener.exitText_prop(self)




    def text_prop(self):

        localctx = SlideParser.Text_propContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_text_prop)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.textCont()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.fontSize()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.fontFam()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.align()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SrcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(SlideParser.STR, 0)

        def getRuleIndex(self):
            return SlideParser.RULE_src

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSrc" ):
                listener.enterSrc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSrc" ):
                listener.exitSrc(self)




    def src(self):

        localctx = SlideParser.SrcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_src)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(SlideParser.T__6)
            self.state = 91
            self.match(SlideParser.STR)
            self.state = 92
            self.match(SlideParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNIDAD(self, i:int=None):
            if i is None:
                return self.getTokens(SlideParser.UNIDAD)
            else:
                return self.getToken(SlideParser.UNIDAD, i)

        def getRuleIndex(self):
            return SlideParser.RULE_position

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosition" ):
                listener.enterPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosition" ):
                listener.exitPosition(self)




    def position(self):

        localctx = SlideParser.PositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_position)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(SlideParser.T__7)
            self.state = 95
            self.match(SlideParser.UNIDAD)
            self.state = 96
            self.match(SlideParser.T__8)
            self.state = 97
            self.match(SlideParser.UNIDAD)
            self.state = 98
            self.match(SlideParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WidthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNIDAD(self):
            return self.getToken(SlideParser.UNIDAD, 0)

        def getRuleIndex(self):
            return SlideParser.RULE_width

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWidth" ):
                listener.enterWidth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWidth" ):
                listener.exitWidth(self)




    def width(self):

        localctx = SlideParser.WidthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_width)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(SlideParser.T__9)
            self.state = 101
            self.match(SlideParser.UNIDAD)
            self.state = 102
            self.match(SlideParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeightContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNIDAD(self):
            return self.getToken(SlideParser.UNIDAD, 0)

        def getRuleIndex(self):
            return SlideParser.RULE_height

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeight" ):
                listener.enterHeight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeight" ):
                listener.exitHeight(self)




    def height(self):

        localctx = SlideParser.HeightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_height)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(SlideParser.T__10)
            self.state = 105
            self.match(SlideParser.UNIDAD)
            self.state = 106
            self.match(SlideParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextContContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(SlideParser.STR, 0)

        def getRuleIndex(self):
            return SlideParser.RULE_textCont

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTextCont" ):
                listener.enterTextCont(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTextCont" ):
                listener.exitTextCont(self)




    def textCont(self):

        localctx = SlideParser.TextContContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_textCont)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(SlideParser.T__11)
            self.state = 109
            self.match(SlideParser.STR)
            self.state = 110
            self.match(SlideParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FontSizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SlideParser.INT, 0)

        def getRuleIndex(self):
            return SlideParser.RULE_fontSize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFontSize" ):
                listener.enterFontSize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFontSize" ):
                listener.exitFontSize(self)




    def fontSize(self):

        localctx = SlideParser.FontSizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_fontSize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(SlideParser.T__12)
            self.state = 113
            self.match(SlideParser.INT)
            self.state = 114
            self.match(SlideParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FontFamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(SlideParser.STR, 0)

        def getRuleIndex(self):
            return SlideParser.RULE_fontFam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFontFam" ):
                listener.enterFontFam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFontFam" ):
                listener.exitFontFam(self)




    def fontFam(self):

        localctx = SlideParser.FontFamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_fontFam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(SlideParser.T__13)
            self.state = 117
            self.match(SlideParser.STR)
            self.state = 118
            self.match(SlideParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALIGN(self):
            return self.getToken(SlideParser.ALIGN, 0)

        def getRuleIndex(self):
            return SlideParser.RULE_align

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlign" ):
                listener.enterAlign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlign" ):
                listener.exitAlign(self)




    def align(self):

        localctx = SlideParser.AlignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_align)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(SlideParser.T__14)
            self.state = 121
            self.match(SlideParser.ALIGN)
            self.state = 122
            self.match(SlideParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





