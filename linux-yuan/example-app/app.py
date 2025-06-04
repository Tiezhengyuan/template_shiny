# pyright: basic

from linux_yuan import linux_yuan

from shiny import App, render, ui

app_ui = ui.page_fluid(
    linux_yuan("myComponent"),
    ui.output_text("valueOut"),
)


def server(input, output, session):
    @render.text
    def valueOut():
        return f"Value from input is {input.myComponent()}"


app = App(app_ui, server)
