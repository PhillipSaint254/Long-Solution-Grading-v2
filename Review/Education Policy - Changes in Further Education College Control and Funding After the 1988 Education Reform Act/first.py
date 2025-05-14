class GetStats:
    def __init__(self):
        self.students_1987 = 530000  # 530k students NAFE in 1987
        self.ssr_1987 = 8.8

    def get_staff_1987(self):
        return self.students_1987 / self.ssr_1987
    
if __name__ == "__main__":
    print(GetStats().get_staff_1987())
