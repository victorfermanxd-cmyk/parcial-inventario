"""
Dashboard de inventario: PyQt5 + Matplotlib + Pandas.
Ejecutar desde la carpeta del proyecto: python app.py
"""
import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QMessageBox, QComboBox
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

CSV_FILE = "datos.csv"

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard de Inventario - Empresa Salvadoreña")
        self.resize(1100, 720)
        try:
            self.df = pd.read_csv(CSV_FILE)
        except Exception as exc:
            QMessageBox.critical(self, "Error", f"No se pudo leer {CSV_FILE}.\n{exc}")
            raise

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        title = QLabel("DASHBOARD DE INVENTARIO POR SUCURSAL")
        title.setStyleSheet("font-size: 22px; font-weight: bold; padding: 8px;")
        layout.addWidget(title)

        controls = QHBoxLayout()
        controls.addWidget(QLabel("Filtrar sucursal:"))
        self.combo = QComboBox()
        self.combo.addItem("Todas las sucursales")
        self.combo.addItems(sorted(self.df["Sucursal"].dropna().unique()))
        self.combo.currentTextChanged.connect(self.update_dashboard)
        controls.addWidget(self.combo)
        refresh = QPushButton("Actualizar gráficos")
        refresh.clicked.connect(self.update_dashboard)
        controls.addWidget(refresh)
        controls.addStretch()
        layout.addLayout(controls)

        self.summary = QLabel()
        self.summary.setStyleSheet("font-size: 14px; padding: 8px; background: #eef3f8;")
        layout.addWidget(self.summary)

        self.figure = Figure(figsize=(10, 5), tight_layout=True)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.update_dashboard()

    def update_dashboard(self):
        branch = self.combo.currentText()
        if branch == "Todas las sucursales":
            data = self.df.copy()
        else:
            data = self.df[self.df["Sucursal"] == branch].copy()

        units = int(data["Cantidad"].sum())
        value = float(data["Valor_Inventario_USD"].sum())
        self.summary.setText(
            f"Registros: {len(data)}   |   Unidades disponibles: {units:,}   |   "
            f"Valor total: ${value:,.2f}"
        )

        self.figure.clear()
        ax1 = self.figure.add_subplot(121)
        ax2 = self.figure.add_subplot(122)

        by_branch = data.groupby("Sucursal")["Cantidad"].sum().sort_values(ascending=False)
        ax1.bar(by_branch.index, by_branch.values)
        ax1.set_title("Unidades por sucursal")
        ax1.set_ylabel("Unidades")
        ax1.tick_params(axis="x", rotation=35)
        ax1.grid(axis="y", alpha=0.25)

        by_category = data.groupby("Categoria")["Valor_Inventario_USD"].sum().sort_values(ascending=False)
        ax2.bar(by_category.index, by_category.values)
        ax2.set_title("Valor del inventario por categoría")
        ax2.set_ylabel("USD ($)")
        ax2.tick_params(axis="x", rotation=45)
        ax2.grid(axis="y", alpha=0.25)

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())
