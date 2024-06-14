import todo_model as model

def get_all_tasks():
    return model.get_all_tasks()

def add_task(titre, description):
    model.add_task(titre, description)

def delete_task(task_id):
    model.delete_task(task_id)
