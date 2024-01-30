from shiny import App, ui
import subprocess
import tempfile
import shutil

app_ui = ui.page_fluid(
    ui.input_slider("n", "Number of points", 1, 100, 50),
    ui.download_button("report", "Generate report"),
)

def server(input, output, session):
    @session.download(filename="report.html")
    def report():
        id = ui.notification_show(
            "Rendering report...",
            duration=None,
            close_button=False
        )

        with tempfile.TemporaryDirectory() as tmpdirname:
            source_file = '/'.join([tmpdirname, "report.qmd"])
            shutil.copy("report.qmd", source_file)
            subprocess.run([
                'quarto', 'render', source_file,
                '-P', f"n:{input.n()}"
            ])

            output_file = '/'.join([tmpdirname, "report.html"])
            html_file = open(output_file, 'r')
            html_docs = html_file.read()

        yield html_docs


app = App(app_ui, server)
