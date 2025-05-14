from first import GetStats as GST

class GetStats(GST):
    def __init__(self):
        super().__init__()
        self.students_1989 = 287000  # from PCFC 1989-90 FTE students
        self.ssr_1989 = 10.8  # approximate SSR for other maintained establishments 1987-88
    
    def get_staff_1989(self):
        return self.students_1989 / self.ssr_1989
    
if __name__ == "__main__":
    print(GetStats().get_staff_1989())
