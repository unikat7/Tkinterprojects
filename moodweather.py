import tkinter as tk
import random

# --- Window Setup ---
window = tk.Tk()
window.title("Mood Weather Machine")
window.resizable(False, False)

CANVAS_W = 500
CANVAS_H = 380

canvas = tk.Canvas(window, width=CANVAS_W, height=CANVAS_H, bg="black")
canvas.pack()

# --- Global State ---
current_mood = None
animation_id = None
particles = []  # list of dicts: {id, x, y, speed, ...}

# ─────────────────────────────────────────
# CLEAR helpers
# ─────────────────────────────────────────
def clear_all():
    global animation_id, particles
    if animation_id:
        window.after_cancel(animation_id)
        animation_id = None
    canvas.delete("all")
    particles = []

# ─────────────────────────────────────────
# HAPPY — sunny sky with bouncing sun rays
# ─────────────────────────────────────────
def draw_happy():
    clear_all()
    # Sky gradient (simulated with rectangles)
    for i in range(CANVAS_H):
        r = int(135 + 120 * i / CANVAS_H)
        g = int(206 - 50 * i / CANVAS_H)
        b = 255
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, CANVAS_W, i, fill=color)

    # Ground
    canvas.create_rectangle(0, 310, CANVAS_W, CANVAS_H, fill="#7ec850", outline="")

    # Sun
    canvas.create_oval(200, 40, 300, 140, fill="#FFD700", outline="#FFA500", width=3, tags="sun")

    # Clouds
    for cx, cy in [(80, 60), (370, 80), (260, 30)]:
        canvas.create_oval(cx, cy, cx+80, cy+40, fill="white", outline="")
        canvas.create_oval(cx+15, cy-15, cx+65, cy+25, fill="white", outline="")

    # Flowers
    for fx in [60, 160, 300, 420]:
        canvas.create_line(fx, 360, fx, 320, fill="green", width=2)
        canvas.create_oval(fx-10, 310, fx+10, 330, fill="#FF69B4", outline="")
        canvas.create_oval(fx-8, 308, fx+8, 324, fill="yellow", outline="")

    label.config(text="😊  You're feeling HAPPY!", bg="#87CEEB", fg="#333")
    animate_happy()

ray_angle = 0
def animate_happy():
    global animation_id, ray_angle
    canvas.delete("rays")
    cx, cy = 250, 90
    import math
    for i in range(8):
        angle = math.radians(ray_angle + i * 45)
        x1 = cx + 55 * math.cos(angle)
        y1 = cy + 55 * math.sin(angle)
        x2 = cx + 75 * math.cos(angle)
        y2 = cy + 75 * math.sin(angle)
        canvas.create_line(x1, y1, x2, y2, fill="#FFD700", width=3, tags="rays")
    ray_angle = (ray_angle + 3) % 360
    animation_id = window.after(40, animate_happy)

# ─────────────────────────────────────────
# SAD — rainy dark sky with falling drops
# ─────────────────────────────────────────
def draw_sad():
    clear_all()
    # Dark sky
    canvas.create_rectangle(0, 0, CANVAS_W, CANVAS_H, fill="#4a5568", outline="")
    canvas.create_rectangle(0, 300, CANVAS_W, CANVAS_H, fill="#5a7a5a", outline="")

    # Dark clouds
    for cx, cy in [(30, 40), (180, 20), (330, 50), (420, 30)]:
        canvas.create_oval(cx, cy, cx+120, cy+60, fill="#2d3748", outline="")
        canvas.create_oval(cx+20, cy-20, cx+100, cy+30, fill="#2d3748", outline="")

    # Initial raindrops
    for _ in range(40):
        x = random.randint(0, CANVAS_W)
        y = random.randint(0, CANVAS_H)
        drop_id = canvas.create_line(x, y, x, y+12, fill="#90cdf4", width=1)
        particles.append({"id": drop_id, "x": x, "y": y, "speed": random.randint(6, 14)})

    label.config(text="😢  You're feeling SAD...", bg="#4a5568", fg="white")
    animate_sad()

def animate_sad():
    global animation_id
    for p in particles:
        p["y"] += p["speed"]
        if p["y"] > CANVAS_H:
            p["y"] = random.randint(-20, 0)
            p["x"] = random.randint(0, CANVAS_W)
        canvas.coords(p["id"], p["x"], p["y"], p["x"], p["y"] + 12)
    animation_id = window.after(30, animate_sad)

# ─────────────────────────────────────────
# ANGRY — stormy red sky with lightning
# ─────────────────────────────────────────
def draw_angry():
    clear_all()
    canvas.create_rectangle(0, 0, CANVAS_W, CANVAS_H, fill="#742a2a", outline="")
    canvas.create_rectangle(0, 300, CANVAS_W, CANVAS_H, fill="#4a1a1a", outline="")

    # Storm clouds
    for cx, cy in [(0, 30), (150, 10), (300, 40), (400, 20)]:
        canvas.create_oval(cx, cy, cx+140, cy+70, fill="#1a202c", outline="")
        canvas.create_oval(cx+20, cy-20, cx+120, cy+40, fill="#2d3748", outline="")

    # Lightning bolts (static)
    for lx in [130, 320]:
        pts = [lx, 100, lx-15, 160, lx+5, 160, lx-20, 230]
        canvas.create_line(pts, fill="#FFD700", width=3)

    label.config(text="😡  You're feeling ANGRY!", bg="#742a2a", fg="white")
    animate_angry()

flash_on = False
def animate_angry():
    global animation_id, flash_on
    flash_on = not flash_on
    flash_color = "#ff6b35" if flash_on else "#742a2a"
    canvas.itemconfig("sky_flash", fill=flash_color)
    # flash the sky subtly
    canvas.delete("sky_flash")
    canvas.create_rectangle(0, 0, CANVAS_W, 10, fill=flash_color, outline="", tags="sky_flash")
    animation_id = window.after(400, animate_angry)

# ─────────────────────────────────────────
# CALM — night sky with twinkling stars
# ─────────────────────────────────────────
def draw_calm():
    clear_all()
    # Night sky
    canvas.create_rectangle(0, 0, CANVAS_W, CANVAS_H, fill="#0d1b2a", outline="")
    canvas.create_rectangle(0, 310, CANVAS_W, CANVAS_H, fill="#1a3a2a", outline="")

    # Moon
    canvas.create_oval(380, 30, 450, 100, fill="#fffde7", outline="#f9a825", width=2)
    canvas.create_oval(400, 25, 460, 90, fill="#0d1b2a", outline="")  # crescent

    # Stars
    for _ in range(60):
        x = random.randint(0, CANVAS_W)
        y = random.randint(0, 280)
        size = random.choice([1, 1, 2, 2, 3])
        star_id = canvas.create_oval(x, y, x+size, y+size, fill="white", outline="", tags="star")
        particles.append({"id": star_id, "x": x, "y": y, "size": size, "visible": True, "delay": random.randint(0, 30)})

    # Hills
    canvas.create_oval(-50, 270, 250, 420, fill="#1a2a1a", outline="")
    canvas.create_oval(200, 280, 560, 430, fill="#152215", outline="")

    label.config(text="😌  You're feeling CALM~", bg="#0d1b2a", fg="#fffde7")
    animate_calm()

twinkle_tick = 0
def animate_calm():
    global animation_id, twinkle_tick
    twinkle_tick += 1
    for p in particles:
        if twinkle_tick % max(1, p["delay"]) == 0:
            p["visible"] = not p["visible"]
            color = "white" if p["visible"] else "#0d1b2a"
            canvas.itemconfig(p["id"], fill=color)
    animation_id = window.after(120, animate_calm)

# ─────────────────────────────────────────
# UI — Mood Buttons
# ─────────────────────────────────────────
btn_frame = tk.Frame(window, bg="#1a1a2e", pady=6)
btn_frame.pack(fill="x")

moods = [
    ("😊 Happy",  "#f6c90e", "#333",    draw_happy),
    ("😢 Sad",    "#63b3ed", "white",   draw_sad),
    ("😡 Angry",  "#fc8181", "white",   draw_angry),
    ("😌 Calm",   "#b794f4", "white",   draw_calm),
]

for text, bg, fg, cmd in moods:
    tk.Button(
        btn_frame, text=text, bg=bg, fg=fg,
        font=("Arial", 13, "bold"),
        relief="flat", padx=14, pady=6,
        activebackground=bg, cursor="hand2",
        command=cmd
    ).pack(side="left", padx=8, pady=4)

label = tk.Label(window, text="👆  Pick a mood to see the weather!",
                 font=("Arial", 13), bg="#1a1a2e", fg="white", pady=8)
label.pack(fill="x")

# Start with a default view
canvas.create_rectangle(0, 0, CANVAS_W, CANVAS_H, fill="#1a1a2e", outline="")
canvas.create_text(CANVAS_W//2, CANVAS_H//2, text="🌈\nChoose your mood above!",
                   fill="white", font=("Arial", 18), justify="center")

window.mainloop()