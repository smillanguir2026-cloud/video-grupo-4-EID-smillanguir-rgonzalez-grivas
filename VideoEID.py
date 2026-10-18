from manim import *

class PresentacionEje4Larga(Scene):
    def construct(self):
        # ==========================================
        # ESCENA 1: Introducción y Pregunta Central (~45s)
        # ==========================================
        logo_uct = Text("UCT - Universidad Católica de Temuco", font_size=22, color=BLUE_B).to_edge(UP)
        titulo = Text("Eje 4: Del símbolo de sumatoria\nal símbolo de integral definida", font_size=32, weight=BOLD).next_to(logo_uct, DOWN, buff=0.3)
        integrantes = Text("Integrantes: Simón Millanguir | Roberto Gonzales | Gabriel Rivas", font_size=18, color=GRAY_A).next_to(titulo, DOWN, buff=0.3)
        
        self.play(Write(logo_uct), Write(titulo), run_time=2)
        self.play(FadeIn(integrantes), run_time=1.5)
        self.wait(5) # Pausa para hablar con calma la intro

        self.play(FadeOut(logo_uct), FadeOut(integrantes), titulo.animate.scale(0.8).to_corner(UL), run_time=1.5)
        
        pregunta_caja = Rectangle(width=11, height=2.5, color=YELLOW, fill_opacity=0.1).shift(DOWN * 0.5)
        pregunta_txt = Paragraph(
            "Pregunta Central:",
            "¿Cómo pasamos de una suma con un número finito",
            "de rectángulos a una integral definida?",
            font_size=24, alignment="center"
        ).move_to(pregunta_caja)

        self.play(Create(pregunta_caja), Write(pregunta_txt), run_time=2)
        self.wait(8) # Pausa para plantear la pregunta central
        self.play(FadeOut(pregunta_caja), FadeOut(pregunta_txt), FadeOut(titulo), run_time=1)

        # ==========================================
        # ESCENA 2: Suma Finita de Riemann (~1m 15s)
        # ==========================================
        titulo_e2 = Text("Suma Finita de Riemann (Discreta)", font_size=28, color=BLUE).to_corner(UL)
        self.play(Write(titulo_e2), run_time=1)

        expr_riemann = MathTex(r"\sum_{i=1}^{n}", r"f(x_i^*)", r"\Delta x", font_size=36).to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.5)
        self.play(Write(expr_riemann), run_time=2)

        axes = Axes(
            x_range=[0, 3, 1], y_range=[0, 6, 1],
            x_length=5.5, y_length=3.8,
            axis_config={"include_numbers": True}
        ).shift(DOWN * 0.6 + LEFT * 2.2)

        curva = axes.plot(lambda x: x**2 + 1, x_range=[0, 2.1], color=BLUE)
        rects_4 = axes.get_riemann_rectangles(curva, x_range=[0, 2], dx=0.5, stroke_color=WHITE, fill_opacity=0.5, color=TEAL)
        lbl_dx = MathTex(r"\Delta x = \frac{b-a}{n}", font_size=22, color=YELLOW).next_to(axes, DOWN)

        self.play(Create(axes), Create(curva), run_time=2)
        self.play(Create(rects_4), Write(lbl_dx), run_time=2)
        self.wait(10) # Tiempo para explicar los n=4 rectángulos y el error

        self.play(FadeOut(titulo_e2), FadeOut(expr_riemann), FadeOut(rects_4), FadeOut(lbl_dx), run_time=1)

        # ==========================================
        # ESCENA 3: El Paso al Límite n -> inf (~1m 30s)
        # ==========================================
        titulo_e3 = Text("Paso al Límite: Refinamiento de la Partición", font_size=28, color=GREEN).to_corner(UL)
        self.play(Write(titulo_e3), run_time=1)

        f_sumatoria = MathTex(r"\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x", font_size=34).to_corner(UR).shift(LEFT * 0.2 + DOWN * 0.5)
        f_integral = MathTex(r"= \int_{a}^{b} f(x) \, dx", font_size=34, color=YELLOW).next_to(f_sumatoria, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(Write(f_sumatoria), run_time=2)
        self.wait(3)

        rects_curr = axes.get_riemann_rectangles(curva, x_range=[0, 2], dx=2/4, color=TEAL, fill_opacity=0.5)
        self.play(Create(rects_curr), run_time=1)

        for n_val in [10, 50, 200]:
            lbl_n = Text(f"n = {n_val} rectángulos", font_size=20, color=YELLOW).next_to(axes, UP)
            rects_next = axes.get_riemann_rectangles(curva, x_range=[0, 2], dx=2/n_val, color=GREEN_B, fill_opacity=0.6)
            self.play(Transform(rects_curr, rects_next), FadeIn(lbl_n), run_time=2)
            self.wait(3) # Pausa larga para mostrar cómo se ajusta a la curva
            self.play(FadeOut(lbl_n), run_time=0.5)

        self.play(TransformFromCopy(f_sumatoria, f_integral), run_time=2)
        self.wait(5)

        self.play(FadeOut(axes), FadeOut(curva), FadeOut(rects_curr), FadeOut(f_sumatoria), FadeOut(f_integral), FadeOut(titulo_e3), run_time=1)

        # ==========================================
        # ESCENA 4: Ejemplo Numérico Resuelto (~1m)
        # ==========================================
        titulo_e4 = Text("Ejemplo Resuelto: f(x) = x² + 1 en [0, 2]", font_size=28, color=YELLOW).to_corner(UL)
        self.play(Write(titulo_e4), run_time=1)

        axes_e4 = Axes(
            x_range=[-0.5, 3, 1], y_range=[0, 6, 1],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": True}
        ).shift(DOWN * 0.5 + LEFT * 2.8)

        curva_e4 = axes_e4.plot(lambda x: x**2 + 1, x_range=[0, 2.1], color=BLUE)
        area_e4 = axes_e4.get_area(curva_e4, x_range=[0, 2], color=GREEN, opacity=0.4)

        self.play(Create(axes_e4), Create(curva_e4), FadeIn(area_e4), run_time=2)
        self.wait(3)

        paso1 = MathTex(r"\int_{0}^{2} (x^2 + 1) \, dx", font_size=28).to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.8)
        paso2 = MathTex(r"= \left[ \frac{x^3}{3} + x \right]_{0}^{2}", font_size=28, color=TEAL).next_to(paso1, DOWN, buff=0.3, aligned_edge=LEFT)
        nota_regla = Text("Regla de potencia: x^2 -> x^3 / 3", font_size=16, color=YELLOW).next_to(paso2, DOWN, buff=0.15, aligned_edge=LEFT)
        res_exacto = MathTex(r"= \frac{14}{3} \approx 4.67 \text{ u}^2", font_size=32, color=GREEN).next_to(nota_regla, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(Write(paso1), run_time=2)
        self.wait(4)
        self.play(Write(paso2), FadeIn(nota_regla), run_time=2)
        self.wait(6) # Pausa clave para explicar la regla de la potencia
        self.play(Write(res_exacto), run_time=2)
        self.wait(6)

        self.play(FadeOut(axes_e4), FadeOut(curva_e4), FadeOut(area_e4), FadeOut(paso1), FadeOut(paso2), FadeOut(nota_regla), FadeOut(res_exacto), FadeOut(titulo_e4), run_time=1)

        # ==========================================
        # ESCENA 5: Conclusión y Referencias (30s)
        # ==========================================
        conclusion_titulo = Text("Conclusión y Referencias", font_size=28, color=GOLD).to_corner(UL)

        res_final = Paragraph(
            "Conclusión: La integral definida representa el límite de la suma de infinitos",
            "rectángulos de ancho infinitesimal, entregando el área geométrica exacta.",
            font_size=20, color=WHITE
        ).next_to(conclusion_titulo, DOWN, buff=0.3, aligned_edge=LEFT)

        refs = Paragraph(
            "Referencias Bibliográficas y Recursos:",
            "• Apunte 'Introducción a la Integral' (Cálculo Intermedio, UCT)",
            "• Stewart, J. (2016). Cálculo de una variable (8va ed.)",
            "• Thomas, G. (2015). Cálculo de una variable (13ra ed.)",
            "• Animaciones realizadas con Manim Community v0.18+",
            "• Declaración de IA: Apoyo en revisión de guion y estructuración de código",
            font_size=18, color=GRAY_A
        ).next_to(res_final, DOWN, buff=0.4, aligned_edge=LEFT)

        self.play(Write(conclusion_titulo), Write(res_final), run_time=2)
        self.play(FadeIn(refs), run_time=2)
        self.wait(10) # Pausa final para la placa de cierre
