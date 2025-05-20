import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox, simpledialog
from datetime import datetime
from tkcalendar import Calendar

from src.constants import APP_NAME, APP_TITLE, WINDOW_SIZE, SQUADS
from src.utils import generate_report, get_lines

class PPPGenerator:
    def __init__(self, root):
        """
        Inicializa a aplicação PPP Generator.
        
        Args:
            root: Janela principal da aplicação Tkinter
        """

        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry(WINDOW_SIZE)
        
        self.style = ttk.Style()
        self.style.configure('TFrame', padding=10)
        self.style.configure('TButton', padding=5)
        
        self.create_widgets()
        self.update_report()
    
    def create_widgets(self):
        """
        Cria e configura todos os widgets da interface gráfica.
        Inclui campos de data, squad, sprint e seções de texto.
        """

        # Definindo largura padrão para os campos (25% da largura da janela)
        field_width = 40 
        label_width = 10 

        # Frame principal com configuração de grid
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Configurar grid
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(5, weight=1)  # Linha do notebook
        main_frame.grid_rowconfigure(7, weight=3)  # Linha da visualização
        
        # Cabeçalho
        ttk.Label(main_frame, text=APP_TITLE, 
                 font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0,10))
        
        # Linha 1 - Data
        date_frame = ttk.Frame(main_frame)
        date_frame.grid(row=1, column=0, sticky="w", pady=5)
        
        label = ttk.Label(date_frame, text="DATA:", width=label_width)
        label.pack(side=tk.LEFT)
        
        self.data_entry = ttk.Entry(date_frame, width=field_width)
        self.data_entry.pack(side=tk.LEFT)
        self.data_entry.insert(0, datetime.now().strftime('%d/%m/%Y'))
        
        # Calendar frame (always visible)
        self.cal_frame = ttk.Frame(main_frame)
        self.cal_frame.grid(row=1, column=1, rowspan=3, padx=10, sticky="ne")
        
        self.cal = Calendar(self.cal_frame, selectmode='day',
                        background='white', foreground='black',
                        selectbackground='blue', selectforeground='white',
                        width=25, height=8)
        self.cal.pack(padx=5, pady=5)
        ttk.Button(self.cal_frame, text="Selecionar", 
                command=self.select_date).pack(pady=5)
        
        self.data_entry.bind("<KeyRelease>", self.update_report)
        
        # Linha 2 - Squad
        squad_frame = ttk.Frame(main_frame)
        squad_frame.grid(row=2, column=0, sticky="w", pady=5)
        
        ttk.Label(squad_frame, text="SQUAD:", width=label_width).pack(side=tk.LEFT)
        self.squad_combo = ttk.Combobox(squad_frame,  
                                    values=SQUADS,
                                    width=field_width-3)
        self.squad_combo.pack(side=tk.LEFT)
        
        # Adicionar botão para novo squad
        # ttk.Button(squad_frame, text="Novo Squad", 
        #           command=self.add_new_squad).pack(side=tk.LEFT, padx=5)


        self.squad_combo.bind("<<ComboboxSelected>>", self.update_report)
        self.squad_combo.bind("<KeyRelease>", self.update_report)
        
        # Linha 3 - Sprint
        sprint_frame = ttk.Frame(main_frame)
        sprint_frame.grid(row=3, column=0, sticky="w", pady=5)
        
        ttk.Label(sprint_frame, text="SPRINT:", width=label_width).pack(side=tk.LEFT)
        self.sprint_entry = ttk.Entry(sprint_frame, width=field_width)
        self.sprint_entry.pack(side=tk.LEFT)

        self.sprint_entry.bind("<KeyRelease>", self.update_report)
        
        # Notebook para as seções (Progressos, Planos, Problemas)
        notebook = ttk.Notebook(main_frame)
        notebook.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")
        
        sections = ["PROGRESSOS", "PLANOS", "PROBLEMAS"]
        self.text_widgets = {}
        
        
        for section in sections:
            frame = ttk.Frame(notebook)
            text = scrolledtext.ScrolledText(frame, width=60, height=8,
                                           wrap=tk.WORD, font=('Arial', 10))
            text.pack(fill=tk.BOTH, expand=True)
            text.bind("<KeyRelease>", self.update_report)
            notebook.add(frame, text=section)
            self.text_widgets[section] = text
        
        visualization_notebook = ttk.Notebook(main_frame)
        visualization_notebook.grid(row=6, column=0, columnspan=2, pady=10, sticky="nsew")
        
        # Criar apenas uma seção para visualização
        frame = ttk.Frame(visualization_notebook)
        self.report_view = scrolledtext.ScrolledText(frame, width=60, height=12,
                                                   wrap=tk.WORD, font=('Arial', 10))
        self.report_view.pack(fill=tk.BOTH, expand=True)
        visualization_notebook.add(frame, text="VISUALIZAÇÃO")
        
        # Botões
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=10)
        
        # Botão "Copiar Relatório" que gera e copia automaticamente
        ttk.Button(btn_frame, text="Copiar Relatório", 
                  command=self.copy_report).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(btn_frame, text="Salvar", 
                  command=self.save_report).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Sair", 
                  command=self.root.quit).pack(side=tk.LEFT, padx=5)
        
    def add_new_squad(self):
        """
        Adiciona um novo squad à lista através de uma caixa de diálogo.
        Capitaliza o nome e verifica duplicatas antes de adicionar.
        """

        new_squad = simpledialog.askstring("Novo Squad", "Digite o nome do novo squad:")
        if new_squad:
            # Capitaliza a primeira letra
            new_squad = new_squad.strip().capitalize()
            
            # Verifica se já existe
            if new_squad not in self.squad_combo['values']:
                # Adiciona à lista e reordena
                current_values = list(self.squad_combo['values'])
                current_values.append(new_squad)
                self.squad_combo['values'] = sorted(current_values)
                
                # Seleciona o novo valor
                self.squad_combo.set(new_squad)
                self.update_report()
            else:
                messagebox.showwarning("Aviso", "Este squad já existe!")

    def toggle_calendar(self):
        """
        Alterna a visibilidade do calendário na interface.
        Controla a exibição/ocultação do widget de calendário.
        """

        if self.calendar_visible:
            self.cal_frame.grid_forget()
            self.cal_btn.config(text="📅")
        else:
            # Position calendar in the red area
            self.cal_frame.grid(row=1, column=1, rowspan=3, padx=10, sticky="ne")
            self.cal_btn.config(text="⬆️")
        self.calendar_visible = not self.calendar_visible
    
    def select_date(self):
        """
        Atualiza a data selecionada no campo de entrada.
        Converte o formato da data do calendário para o formato brasileiro.
        """
        selected_date = self.cal.get_date()

        date_obj = datetime.strptime(selected_date, '%m/%d/%y')
        formatted_date = date_obj.strftime('%d/%m/%Y')
        
        self.data_entry.delete(0, tk.END)
        self.data_entry.insert(0, formatted_date)
        self.update_report()
    
    def on_squad_key(self, event):
        """
        Manipula eventos de tecla no combobox de squad.
        
        Args:
            event: Evento de tecla capturado
        """

        if event.char.isalpha():
            current = self.squad_combo.get()
            if current not in self.squad_combo["values"]:
                self.squad_combo["values"] = tuple(list(self.squad_combo["values"]) + [current])
    

    def update_report(self, event=None):
        """
        Atualiza o relatório em tempo real na visualização.
        
        Args:
            event: Evento que triggered a atualização (opcional)
        """
        progressos = get_lines(self.text_widgets["PROGRESSOS"])
        planos = get_lines(self.text_widgets["PLANOS"])
        problemas = get_lines(self.text_widgets["PROBLEMAS"])
        
        report = generate_report(
            self.data_entry.get(),
            self.squad_combo.get(),
            self.sprint_entry.get(),
            progressos,
            planos,
            problemas
        )
        
        self.report_view.delete(1.0, tk.END)
        self.report_view.insert(tk.END, report)
    
    def copy_report(self):
        """
        Copia o relatório atual para a área de transferência.
        Exibe mensagem de confirmação após a cópia.
        """

        report = self.report_view.get(1.0, tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(report)
        messagebox.showinfo("Copiado", "Relatório copiado para a área de transferência!")
    
    def save_report(self):
        """
        Salva o relatório atual em um arquivo de texto.
        Permite escolher local e nome do arquivo.
        Trata possíveis erros durante o salvamento.
        """
        report = self.report_view.get(1.0, tk.END)
        if not report.strip():
            messagebox.showwarning("Aviso", "Gere um relatório antes de salvar!")
            return
            
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de Texto", "*.txt")],
            initialfile=f"PPP_REPORT_{self.data_entry.get().replace('/', '-')}.txt"
        )
        
        if filepath:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(report)
                messagebox.showinfo("Sucesso", "Relatório salvo com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao salvar:\n{str(e)}")
