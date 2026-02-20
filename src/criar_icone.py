from PIL import Image, ImageDraw

# Cria uma imagem 256x256 com fundo azul escuro
img = Image.new('RGB', (256, 256), color='#1e3a5f')
draw = ImageDraw.Draw(img)

# Desenha um HD/disco (representando armazenamento)
# Corpo do HD - retângulo arredondado (aproximado com retângulo)
draw.rectangle([40, 80, 160, 160], fill='#2E7D32', outline='#1B5E20', width=3)

# Placa do HD com listras (para fazer parecer mais realista)
draw.rectangle([50, 95, 150, 145], fill='#4CAF50', outline='#2E7D32', width=2)
draw.line([(50, 105), (150, 105)], fill='#1B5E20', width=2)
draw.line([(50, 115), (150, 115)], fill='#1B5E20', width=2)
draw.line([(50, 125), (150, 125)], fill='#1B5E20', width=2)
draw.line([(50, 135), (150, 135)], fill='#1B5E20', width=2)

# Círculo (representando carcaça)
draw.ellipse([45, 75, 155, 165], outline='#1B5E20', width=3)

# Seta grande de download/backup (vertical)
arrow_x, arrow_y = 200, 150
arrow_size = 35

# Haste da seta
draw.rectangle([arrow_x - 5, arrow_y - arrow_size, arrow_x + 5, arrow_y + 10], fill='#FFC107', outline='#FFA000', width=2)

# Ponta da seta (triângulo)
draw.polygon(
    [(arrow_x, arrow_y + 10), 
     (arrow_x - 15, arrow_y - 10), 
     (arrow_x + 15, arrow_y - 10)],
    fill='#FFC107', outline='#FFA000'
)

# Salva como PNG
img.save('backup_icone.png')

# Converte para ICO
img.save('backup_icone.ico')

print("backup_icone.png criado (HD + seta)")
print("backup_icone.ico criado (HD + seta)")
