from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)

from matplotlib.figure import Figure

from cube_modules.cube_renderer import CubeRenderer
from cube_modules.cube import CubeBuilder

from cube_modules.app import Application


class WorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)
    fps = QtCore.pyqtSignal(float)


class CubeWorker(QtCore.QRunnable):
    def __init__(self, canvas, application):
        super(CubeWorker, self).__init__()
        self.canvas = canvas
        self.signals = WorkerSignals()
        self.application = application

    def run(self):
        try:
            self.application.run()
            self.signals.result.emit('Command Received')
        except Exception as e:
            self.signals.error.emit((type(e), str(e)))
        finally:
            self.signals.finished.emit()


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig = Figure()
        super(MplCanvas, self).__init__(fig)
        self.setParent(parent)

        self.ax = self.figure.add_subplot(111, projection='3d')
        self.ax.view_init(elev=15, azim=45)

        self.application = Application(self)
        self.threadpool = QtCore.QThreadPool()
        self.start_worker()

    def start_worker(self):
        worker = CubeWorker(self, self.application)
        worker.signals.finished.connect(self.worker_finished)
        self.threadpool.start(worker)

    def worker_finished(self):
        self.application.renderer.render()
        self.start_worker()


class TopLevelWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("[CubeTutor] 3D Render")
        self.canvas = MplCanvas()
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.canvas)
