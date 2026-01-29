import json
import requests
from tkinter import *
from tkinter import ttk, messagebox
import threading

class GitHubRepoInfo:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Repository Information")
        self.root.geometry("600x400")

        # Список репозиториев для разных вариантов
        # По последней цифре зачетки 7 выбираем вариант 7
        self.repositories = {
            'freeCodeCamp': 'https://api.github.com/users/freeCodeCamp',
            'vuejs': 'https://api.github.com/users/vuejs',
            'facebook': 'https://api.github.com/users/facebook',
            'tensorflow': 'https://api.github.com/users/tensorflow',
            'Microsoft': 'https://api.github.com/users/Microsoft',
            'google': 'https://api.github.com/users/google',
            'kubernetes': 'https://api.github.com/users/kubernetes',  # Вариант 7
            'docker': 'https://api.github.com/users/docker',
            'apple': 'https://api.github.com/users/apple',
            'mozilla': 'https://api.github.com/users/mozilla'
        }

        self.setup_ui()

    def setup_ui(self):
        # Заголовок
        title_label = Label(self.root, text="GitHub Repository Information",
                            font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Описание
        desc_label = Label(self.root, text="Введите имя репозитория и нажмите 'Получить информацию'",
                           font=("Arial", 10))
        desc_label.pack(pady=5)

        # Ваш вариант
        variant_label = Label(self.root, text="Ваш вариант (по последней цифре зачетки 7): kubernetes",
                              font=("Arial", 10, "bold"), fg="blue")
        variant_label.pack(pady=5)

        # Frame для ввода
        input_frame = Frame(self.root)
        input_frame.pack(pady=20)

        Label(input_frame, text="Имя репозитория:", font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5)

        # Поле ввода с подсказкой
        self.repo_entry = ttk.Entry(input_frame, width=30, font=("Arial", 11))
        self.repo_entry.grid(row=0, column=1, padx=5, pady=5)
        self.repo_entry.insert(0, "kubernetes")  # Предзаполняем вариантом 7

        # Кнопка получения информации
        self.get_btn = ttk.Button(input_frame, text="Получить информацию",
                                  command=self.get_repo_info_thread)
        self.get_btn.grid(row=0, column=2, padx=10, pady=5)

        # Кнопка для получения информации по вашему варианту
        self.variant_btn = ttk.Button(input_frame, text="Мой вариант (7)",
                                      command=lambda: self.get_variant_info("kubernetes"))
        self.variant_btn.grid(row=1, column=1, padx=5, pady=10)

        # Поле для вывода информации
        output_frame = Frame(self.root)
        output_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

        Label(output_frame, text="Информация о репозитории:",
              font=("Arial", 11, "bold")).pack(anchor=W)

        # Текстовое поле с прокруткой для вывода информации
        text_frame = Frame(output_frame)
        text_frame.pack(fill=BOTH, expand=True, pady=5)

        self.info_text = Text(text_frame, height=10, font=("Courier", 10), wrap=WORD)
        scrollbar = Scrollbar(text_frame, command=self.info_text.yview)
        self.info_text.configure(yscrollcommand=scrollbar.set)

        self.info_text.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Статус бар
        self.status_var = StringVar()
        self.status_var.set("Готово")
        status_bar = Label(self.root, textvariable=self.status_var,
                           bd=1, relief=SUNKEN, anchor=W)
        status_bar.pack(side=BOTTOM, fill=X)

        # Подсказка
        hint_label = Label(self.root,
                           text="Примеры репозиториев: freeCodeCamp, vuejs, facebook, tensorflow, Microsoft, google, kubernetes, docker, apple, mozilla",
                           font=("Arial", 9), fg="gray")
        hint_label.pack(pady=10)

    def get_repo_info_thread(self):
        """Запуск получения информации в отдельном потоке"""
        repo_name = self.repo_entry.get().strip()
        if not repo_name:
            messagebox.showwarning("Предупреждение", "Введите имя репозитория")
            return

        # Отключаем кнопку на время выполнения
        self.get_btn.config(state=DISABLED)
        self.status_var.set("Получение информации...")

        # Запуск в отдельном потоке
        thread = threading.Thread(target=self.get_repo_info, args=(repo_name,))
        thread.daemon = True
        thread.start()

    def get_repo_info(self, repo_name):
        """Получение информации о репозитории"""
        try:
            # Формируем URL для API GitHub
            url = f"https://api.github.com/users/{repo_name}"

            # Отправляем GET-запрос
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()

                # Формируем данные в требуемом формате
                result_data = {
                    'company': data.get('company'),
                    'created_at': data.get('created_at'),
                    'email': data.get('email'),
                    'id': data.get('id'),
                    'name': data.get('name'),
                    'url': data.get('url')
                }

                # Сохраняем в файл
                filename = f"{repo_name}_info.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(result_data, f, indent=4, ensure_ascii=False)

                # Выводим информацию в текстовое поле
                self.display_info(result_data, filename)
                self.status_var.set(f"Информация сохранена в {filename}")

            elif response.status_code == 404:
                messagebox.showerror("Ошибка", f"Репозиторий '{repo_name}' не найден")
                self.status_var.set("Репозиторий не найден")
            else:
                messagebox.showerror("Ошибка", f"Ошибка API: {response.status_code}")
                self.status_var.set(f"Ошибка: {response.status_code}")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Ошибка", f"Ошибка соединения: {str(e)}")
            self.status_var.set("Ошибка соединения")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Неизвестная ошибка: {str(e)}")
            self.status_var.set("Ошибка")
        finally:
            # Включаем кнопку обратно
            self.root.after(0, lambda: self.get_btn.config(state=NORMAL))

    def get_variant_info(self, repo_name):
        """Получение информации для вашего варианта"""
        self.repo_entry.delete(0, END)
        self.repo_entry.insert(0, repo_name)
        self.get_repo_info_thread()

    def display_info(self, data, filename):
        """Отображение информации в текстовом поле"""
        self.info_text.delete(1.0, END)

        info_str = "=" * 50 + "\n"
        info_str += "ИНФОРМАЦИЯ О РЕПОЗИТОРИИ\n"
        info_str += "=" * 50 + "\n\n"

        for key, value in data.items():
            info_str += f"{key}: {value}\n"

        info_str += "\n" + "=" * 50 + "\n"
        info_str += f"Данные сохранены в файл: {filename}\n"
        info_str += "=" * 50

        self.info_text.insert(1.0, info_str)

        # Также выводим в консоль для проверки
        print(info_str)

        # Открываем файл для просмотра содержимого
        self.show_file_content(filename)

    def show_file_content(self, filename):
        """Показ содержимого сохраненного файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            # Добавляем содержимое файла в текстовое поле
            self.info_text.insert(END, "\n\n" + "=" * 50 + "\n")
            self.info_text.insert(END, "СОДЕРЖИМОЕ ФАЙЛА:\n")
            self.info_text.insert(END, "=" * 50 + "\n\n")
            self.info_text.insert(END, content)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось прочитать файл: {str(e)}")

def main():
    root = Tk()
    app = GitHubRepoInfo(root)
    root.mainloop()


if __name__ == "__main__":
    main()