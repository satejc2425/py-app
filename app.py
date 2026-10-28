from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage with completion status
tasks = [
    {"id": 1, "text": "Learn Flask", "done": False},
    {"id": 2, "text": "Build a Docker container", "done": False},
    {"id": 3, "text": "Deploy the application", "done": False}
]
next_id = 4

@app.route("/", methods=["GET", "POST"])
def index():
    global next_id
    if request.method == "POST":
        task_name = request.form.get("task")
        if task_name:
            tasks.append({"id": next_id, "text": task_name, "done": False})
            next_id += 1
        return redirect(url_for("index"))

    return render_template("index.html", tasks=tasks)

@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
