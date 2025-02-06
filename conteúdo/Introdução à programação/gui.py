import flet as ft
import elevador as EE
import time

elevadores, sim = EE.init_sim()
def loop_de_evento(n, page):
    CICLOS=0
    i=0
    EE.sim = sim
    EE.elevadores = elevadores
    entregas = []
    while True:
        # gera_fila()
        EE.gera_fila_bench(i)
        EE.operação()
        EE.saidas()
        if sim['fila'] > 0:
            EE.atualiza_chamadas(0) # Chama os elevadores para o andar 0 caso tenha fila
        if i == n:
            break
        CICLOS += 1
        i += 1
        print(i)
        time.sleep(1)
        atualiza_mostradores(page.most1, elevadores[0]['andar'])
        atualiza_mostradores(page.most2, elevadores[1]['andar'])
        page.update()

def atualiza_mostradores(m, val):
    m.value = str(val)
def main(page: ft.Page):
    page.title = "Painel de Controle do Elevador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

    page.most1 = ft.TextField(value=0, label='Elevador 1', bgcolor=ft.colors.GREEN_200)
    page.most2 = ft.TextField(value=0, label='Elevador 2', bgcolor=ft.colors.GREEN_200)

    page.add(
        ft.Row(
            controls=[page.most1, page.most2],
            spacing=15
        )
    )
    loop_de_evento(100, page)


ft.app(main)
