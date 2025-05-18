# Generated from Slide.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SlideParser import SlideParser
else:
    from SlideParser import SlideParser

# This class defines a complete listener for a parse tree produced by SlideParser.
class SlideListener(ParseTreeListener):

    # Enter a parse tree produced by SlideParser#prog.
    def enterProg(self, ctx:SlideParser.ProgContext):
        pass

    # Exit a parse tree produced by SlideParser#prog.
    def exitProg(self, ctx:SlideParser.ProgContext):
        pass


    # Enter a parse tree produced by SlideParser#stat.
    def enterStat(self, ctx:SlideParser.StatContext):
        pass

    # Exit a parse tree produced by SlideParser#stat.
    def exitStat(self, ctx:SlideParser.StatContext):
        pass


    # Enter a parse tree produced by SlideParser#expr.
    def enterExpr(self, ctx:SlideParser.ExprContext):
        pass

    # Exit a parse tree produced by SlideParser#expr.
    def exitExpr(self, ctx:SlideParser.ExprContext):
        pass


    # Enter a parse tree produced by SlideParser#slide.
    def enterSlide(self, ctx:SlideParser.SlideContext):
        pass

    # Exit a parse tree produced by SlideParser#slide.
    def exitSlide(self, ctx:SlideParser.SlideContext):
        pass


    # Enter a parse tree produced by SlideParser#text.
    def enterText(self, ctx:SlideParser.TextContext):
        pass

    # Exit a parse tree produced by SlideParser#text.
    def exitText(self, ctx:SlideParser.TextContext):
        pass


    # Enter a parse tree produced by SlideParser#img.
    def enterImg(self, ctx:SlideParser.ImgContext):
        pass

    # Exit a parse tree produced by SlideParser#img.
    def exitImg(self, ctx:SlideParser.ImgContext):
        pass


    # Enter a parse tree produced by SlideParser#transform.
    def enterTransform(self, ctx:SlideParser.TransformContext):
        pass

    # Exit a parse tree produced by SlideParser#transform.
    def exitTransform(self, ctx:SlideParser.TransformContext):
        pass


    # Enter a parse tree produced by SlideParser#text_prop.
    def enterText_prop(self, ctx:SlideParser.Text_propContext):
        pass

    # Exit a parse tree produced by SlideParser#text_prop.
    def exitText_prop(self, ctx:SlideParser.Text_propContext):
        pass


    # Enter a parse tree produced by SlideParser#src.
    def enterSrc(self, ctx:SlideParser.SrcContext):
        pass

    # Exit a parse tree produced by SlideParser#src.
    def exitSrc(self, ctx:SlideParser.SrcContext):
        pass


    # Enter a parse tree produced by SlideParser#bg.
    def enterBg(self, ctx:SlideParser.BgContext):
        pass

    # Exit a parse tree produced by SlideParser#bg.
    def exitBg(self, ctx:SlideParser.BgContext):
        pass


    # Enter a parse tree produced by SlideParser#position.
    def enterPosition(self, ctx:SlideParser.PositionContext):
        pass

    # Exit a parse tree produced by SlideParser#position.
    def exitPosition(self, ctx:SlideParser.PositionContext):
        pass


    # Enter a parse tree produced by SlideParser#rotation.
    def enterRotation(self, ctx:SlideParser.RotationContext):
        pass

    # Exit a parse tree produced by SlideParser#rotation.
    def exitRotation(self, ctx:SlideParser.RotationContext):
        pass


    # Enter a parse tree produced by SlideParser#width.
    def enterWidth(self, ctx:SlideParser.WidthContext):
        pass

    # Exit a parse tree produced by SlideParser#width.
    def exitWidth(self, ctx:SlideParser.WidthContext):
        pass


    # Enter a parse tree produced by SlideParser#height.
    def enterHeight(self, ctx:SlideParser.HeightContext):
        pass

    # Exit a parse tree produced by SlideParser#height.
    def exitHeight(self, ctx:SlideParser.HeightContext):
        pass


    # Enter a parse tree produced by SlideParser#textCont.
    def enterTextCont(self, ctx:SlideParser.TextContContext):
        pass

    # Exit a parse tree produced by SlideParser#textCont.
    def exitTextCont(self, ctx:SlideParser.TextContContext):
        pass


    # Enter a parse tree produced by SlideParser#fontSize.
    def enterFontSize(self, ctx:SlideParser.FontSizeContext):
        pass

    # Exit a parse tree produced by SlideParser#fontSize.
    def exitFontSize(self, ctx:SlideParser.FontSizeContext):
        pass


    # Enter a parse tree produced by SlideParser#fontFam.
    def enterFontFam(self, ctx:SlideParser.FontFamContext):
        pass

    # Exit a parse tree produced by SlideParser#fontFam.
    def exitFontFam(self, ctx:SlideParser.FontFamContext):
        pass


    # Enter a parse tree produced by SlideParser#align.
    def enterAlign(self, ctx:SlideParser.AlignContext):
        pass

    # Exit a parse tree produced by SlideParser#align.
    def exitAlign(self, ctx:SlideParser.AlignContext):
        pass



del SlideParser