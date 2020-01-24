import shutil

class Disk:

    def __init__(self):
        self.alocated = 0

    def alocate(self, requested_space=0):
        free_space = self.free_space()
        if requested_space > free_space:
            raise ValueError("You just have {0:.2f} GB free on disk!".format(free_space))
        self.alocated += requested_space

    def free_space(self):
        disk_usage = shutil.disk_usage("/")
        free_space = ((disk_usage.free / 1024) / 1024) / 1024
        return (free_space * 0.9) - self.alocated
