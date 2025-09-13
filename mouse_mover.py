import sys
import time
import random
import pyautogui
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import QThread, QObject, pyqtSignal, pyqtSlot

class MouseWorker(QObject):
    finished = pyqtSignal()
    status_update = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def __init__(self, interval):
        super().__init__()
        self.interval = interval
        self._is_running = True

    @pyqtSlot()
    def run(self):
        if getattr(sys, 'frozen', False):
            pyautogui.FAILSAFE = False

        try:
            screenWidth, screenHeight = pyautogui.size()
            
            while self._is_running:
                for _ in range(self.interval):
                    if not self._is_running:
                        break
                    time.sleep(1)
                
                if not self._is_running:
                    break
                    
                randomX = random.randint(0, screenWidth - 1)
                randomY = random.randint(0, screenHeight - 1)
                pyautogui.moveTo(randomX, randomY, duration=0.5)
                
                status_text = f"Moved to ({randomX}, {randomY})"
                self.status_update.emit(status_text)

        except Exception as e:
            error_message = f"An error occurred: {e}"
            self.error_occurred.emit(error_message)
        finally:
            self.finished.emit()

    def stop(self):
        self._is_running = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Mover")
        self.setFixedSize(350, 200)

        self.thread = None
        self.worker = None

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        central_widget.setLayout(main_layout)
        
        interval_layout = QHBoxLayout()
        interval_layout.addWidget(QLabel("Move mouse every (seconds):"))
        self.interval_entry = QLineEdit("10")
        self.interval_entry.setFixedWidth(50)
        interval_layout.addWidget(self.interval_entry)
        main_layout.addLayout(interval_layout)
        
        self.status_label = QLabel("Status: Stopped")
        main_layout.addWidget(self.status_label)
        
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.exit_button = QPushButton("Exit")
        
        self.start_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px; padding: 5px;")
        self.stop_button.setStyleSheet("background-color: #FFC107; color: black; border-radius: 5px; padding: 5px;")
        self.exit_button.setStyleSheet("background-color: #F44336; color: white; border-radius: 5px; padding: 5px;")
        
        self.stop_button.setEnabled(False)
        
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.exit_button)
        main_layout.addLayout(button_layout)

        self.start_button.clicked.connect(self.start_moving)
        self.stop_button.clicked.connect(self.stop_moving)
        self.exit_button.clicked.connect(self.close)

    def start_moving(self):
        if self.thread and self.thread.isRunning():
            return

        try:
            interval = int(self.interval_entry.text())
            if interval <= 0:
                QMessageBox.critical(self, "Invalid Input", "Interval must be a positive number.")
                return
        except ValueError:
            QMessageBox.critical(self, "Invalid Input", "Please enter a valid number for the interval.")
            return
        
        self.thread = QThread()
        self.worker = MouseWorker(interval=interval)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.status_update.connect(self.update_status_label)
        self.worker.error_occurred.connect(self.show_error_message)

        self.thread.start()

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.status_label.setText("Status: Running...")

    def stop_moving(self):
        if self.thread and self.thread.isRunning():
            if self.worker:
                self.worker.stop()
            self.thread.quit()
            self.thread.wait()
        
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.status_label.setText("Status: Stopped")

    def update_status_label(self, text):
        self.status_label.setText(text)

    def show_error_message(self, text):
        QMessageBox.critical(self, "Error", text)
        self.stop_moving()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.aboutToQuit.connect(window.stop_moving)
    window.show()
    sys.exit(app.exec())


