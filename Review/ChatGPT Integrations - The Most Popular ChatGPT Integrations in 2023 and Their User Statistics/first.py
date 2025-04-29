class GetPercentage:
    def __init__(self):
        self.total_chatgpt_users = 180_000_000  # 180 million
        self.snap_users = 150_000_000
        self.bing_users = 100_000_000
        self.duolingo_users = 74_100_000  # 74.1 million
        self.api_developers = 2_000_000
        self.khanmigo_users = 500_000  # half a million
    
    def get_total_chatgpt_users(self):
        return self.total_chatgpt_users
    
    def get_snap_users(self):
        return self.snap_users
    
    def get_bing_users(self):
        return self.bing_users
    
    def get_duolingo_users(self):
        return self.duolingo_users
    
    def get_api_developers(self):
        return self.api_developers
    
    def get_khanmigo_users(self):
        return self.khanmigo_users
    
    def get_percentages(self):
        total_chatgpt_users = self.get_total_chatgpt_users()  # 180 million
        snap_users = self.get_snap_users()
        bing_users = self.get_bing_users()
        duolingo_users = self.get_duolingo_users()  # 74.1 million
        api_developers = self.get_api_developers()
        khanmigo_users = self.get_khanmigo_users()  # half a million

        return {
            'Snap My AI': snap_users / total_chatgpt_users * 100,
            'Bing Chat': bing_users / total_chatgpt_users * 100,
            'Duolingo': duolingo_users / total_chatgpt_users * 100,
            'OpenAI API Developers': api_developers / total_chatgpt_users * 100,
            'Khanmigo': khanmigo_users / total_chatgpt_users * 100,
        }

if __name__ == "__main__":
    print(GetPercentage().get_percentages())
