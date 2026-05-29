import flet as ft
import elevador as EE
import asyncio

ANDARES = EE.ANDARES
ALTURA_PREDIO = 520
ALTURA_ANDAR = ALTURA_PREDIO / (ANDARES + 1)

elevadores, sim = EE.init_sim()


def border_all(width, color):
    side = ft.BorderSide(width, color)
    return ft.Border(top=side, bottom=side, left=side, right=side)


def calc_pos(andar):
    return ALTURA_PREDIO - (andar + 1) * ALTURA_ANDAR


async def loop_de_evento(n, page):
    i = 0
    EE.sim = sim
    EE.elevadores = elevadores
    while True:
        EE.gera_fila_bench(i)
        EE.operação()
        EE.saidas()
        if sim['fila'] > 0:
            EE.atualiza_chamadas(0)
        if i == n:
            break
        i += 1

        e1 = elevadores[0]
        e2 = elevadores[1]

        page.elev1.top = calc_pos(e1['andar'])
        page.elev1.content.value = str(e1['npass'])
        page.elev1.bgcolor = (
            ft.Colors.BLUE_700 if e1['direção'] == 1
            else ft.Colors.BLUE_400 if e1['direção'] == -1
            else ft.Colors.BLUE_500
        )

        page.elev2.top = calc_pos(e2['andar'])
        page.elev2.content.value = str(e2['npass'])
        page.elev2.bgcolor = (
            ft.Colors.RED_700 if e2['direção'] == 1
            else ft.Colors.RED_400 if e2['direção'] == -1
            else ft.Colors.RED_500
        )

        efic = EE.DESEMBARCADOS / EE.ANDARES_PERCORRIDOS if EE.ANDARES_PERCORRIDOS > 0 else 0.0
        dir1 = "UP" if e1['direção'] == 1 else ("DN" if e1['direção'] == -1 else "IDLE")
        dir2 = "UP" if e2['direção'] == 1 else ("DN" if e2['direção'] == -1 else "IDLE")

        page.stats_map['fila'].value = str(sim['fila'])
        page.stats_map['ciclo'].value = str(i)
        page.stats_map['emb'].value = str(EE.EMBARCADOS)
        page.stats_map['desemb'].value = str(EE.DESEMBARCADOS)
        page.stats_map['perc'].value = str(EE.ANDARES_PERCORRIDOS)
        page.stats_map['efic'].value = f"{efic:.3f}"
        page.stats_map['e1_andar'].value = str(e1['andar'])
        page.stats_map['e1_pass'].value = str(e1['npass'])
        page.stats_map['e1_dir'].value = dir1
        page.stats_map['e1_cham'].value = str(e1['chamadas'])
        page.stats_map['e2_andar'].value = str(e2['andar'])
        page.stats_map['e2_pass'].value = str(e2['npass'])
        page.stats_map['e2_dir'].value = dir2
        page.stats_map['e2_cham'].value = str(e2['chamadas'])

        page.update()
        await asyncio.sleep(1)


def criar_predio():
    controles = []

    controles.append(
        ft.Container(
            border=border_all(3, ft.Colors.GREY_800),
            width=130,
            height=ALTURA_PREDIO,
            top=0,
            left=0,
            border_radius=8,
            bgcolor=ft.Colors.GREY_50,
        )
    )

    for i in range(ANDARES + 1):
        y_base = calc_pos(i)
        controles.append(
            ft.Container(
                content=ft.Text(
                    f"{i:02d}", size=11, color=ft.Colors.GREY_600,
                    weight=ft.FontWeight.BOLD,
                ),
                top=y_base,
                left=4,
                width=22,
                height=ALTURA_ANDAR,
                alignment=ft.Alignment.CENTER_RIGHT,
            )
        )
        controles.append(
            ft.Container(
                bgcolor=ft.Colors.GREY_300,
                top=y_base + ALTURA_ANDAR,
                left=26,
                width=100,
                height=1,
            )
        )

    controles.append(
        ft.Container(
            bgcolor=ft.Colors.GREY_400,
            top=0, left=60, width=1, height=ALTURA_PREDIO,
        )
    )

    elev1 = ft.Container(
        bgcolor=ft.Colors.BLUE_500,
        width=28,
        height=ALTURA_ANDAR - 4,
        top=calc_pos(0) + 2,
        left=30,
        border_radius=4,
        animate_position=ft.Animation(400, ft.AnimationCurve.EASE_IN_OUT),
        content=ft.Text("0", size=12, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
        alignment=ft.Alignment.CENTER,
    )

    elev2 = ft.Container(
        bgcolor=ft.Colors.RED_500,
        width=28,
        height=ALTURA_ANDAR - 4,
        top=calc_pos(0) + 2,
        left=68,
        border_radius=4,
        animate_position=ft.Animation(400, ft.AnimationCurve.EASE_IN_OUT),
        content=ft.Text("0", size=12, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
        alignment=ft.Alignment.CENTER,
    )

    controles.extend([elev1, elev2])

    return (
        ft.Stack(controls=controles, width=130, height=ALTURA_PREDIO),
        elev1, elev2,
    )


def linha(label, value_ctrl):
    return ft.Row(
        [ft.Text(label, size=12, width=110), value_ctrl],
        spacing=4,
    )


def criar_stats():
    stats = {}

    stats['fila'] = ft.Text("0", size=12, weight=ft.FontWeight.BOLD)
    stats['ciclo'] = ft.Text("0", size=12, weight=ft.FontWeight.BOLD)
    stats['emb'] = ft.Text("0", size=12, weight=ft.FontWeight.BOLD)
    stats['desemb'] = ft.Text("0", size=12, weight=ft.FontWeight.BOLD)
    stats['perc'] = ft.Text("0", size=12, weight=ft.FontWeight.BOLD)
    stats['efic'] = ft.Text("0.000", size=12, weight=ft.FontWeight.BOLD)

    stats['e1_andar'] = ft.Text("0", size=12, weight=ft.FontWeight.BOLD)
    stats['e1_pass'] = ft.Text("0", size=12, weight=ft.FontWeight.BOLD)
    stats['e1_dir'] = ft.Text("IDLE", size=12, weight=ft.FontWeight.BOLD)
    stats['e1_cham'] = ft.Text("[]", size=11)

    stats['e2_andar'] = ft.Text("0", size=12, weight=ft.FontWeight.BOLD)
    stats['e2_pass'] = ft.Text("0", size=12, weight=ft.FontWeight.BOLD)
    stats['e2_dir'] = ft.Text("IDLE", size=12, weight=ft.FontWeight.BOLD)
    stats['e2_cham'] = ft.Text("[]", size=11)

    panel = ft.Column([
        ft.Text("Simulacao", size=15, weight=ft.FontWeight.BOLD),
        ft.Divider(height=1),
        linha("Ciclo:", stats['ciclo']),
        linha("Fila:", stats['fila']),
        linha("Embarcados:", stats['emb']),
        linha("Desembarcados:", stats['desemb']),
        linha("Andares Perc.:", stats['perc']),
        linha("Eficiencia:", stats['efic']),
        ft.Divider(height=8),
        ft.Text("Elevador 1", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_600),
        ft.Divider(height=1),
        linha("Andar:", stats['e1_andar']),
        linha("Passageiros:", stats['e1_pass']),
        linha("Direcao:", stats['e1_dir']),
        linha("Chamadas:", stats['e1_cham']),
        ft.Divider(height=8),
        ft.Text("Elevador 2", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_600),
        ft.Divider(height=1),
        linha("Andar:", stats['e2_andar']),
        linha("Passageiros:", stats['e2_pass']),
        linha("Direcao:", stats['e2_dir']),
        linha("Chamadas:", stats['e2_cham']),
    ], spacing=2)

    return panel, stats


async def main(page: ft.Page):
    page.title = "Simulador de Elevadores"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20

    predio, elev1, elev2 = criar_predio()
    page.elev1 = elev1
    page.elev2 = elev2

    stats_panel, stats_map = criar_stats()
    page.stats_map = stats_map

    page.add(
        ft.Row([
            ft.Column([
                ft.Text("Predio", size=16, weight=ft.FontWeight.BOLD),
                predio,
            ], spacing=5),
            ft.VerticalDivider(width=30),
            ft.Container(
                content=stats_panel,
                width=250,
                padding=12,
                border=border_all(1, ft.Colors.GREY_300),
                border_radius=8,
                bgcolor=ft.Colors.GREY_50,
            ),
        ], spacing=10, alignment=ft.MainAxisAlignment.CENTER)
    )

    await loop_de_evento(100, page)


ft.app(main)
