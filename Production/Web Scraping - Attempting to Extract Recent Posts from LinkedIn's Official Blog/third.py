# idefine the five content strings

contents = {}

contents['post1'] = ("AI is changing work, and businesses and professionals are having to adapt. "
                     "LinkedIn’s inaugural Work Change Report: AI Is Coming to Work, reveals how AI is creating new jobs and skills, transforming careers, and spurring productivity and innovation.")

contents['post2'] = ("Today we’re updating our User Agreement and clarifying some practices covered "
                     "by our Privacy Policy.* In our User Agreement, updates include more details on content recommendation...")

contents['post3'] = ("LinkedIn was founded with a vision to create economic opportunity for every "
                     "member of the global workforce. In this post, they share their Responsible AI Principles that guide their work with AI.")

contents['post4'] = ("Today, lead attorney Sarah Wight shared an update on LinkedIn about the hiQ "
                     "court ruling that LinkedIn may enforce its User Agreement against data scraping.")

contents['post5'] = ("Addressing bias is a step on our journey to help drive equitable outcomes for "
                     "all members of the global workforce. An important component of this work centers on our LinkedIn Feed...")

# function to get first 100 chars
def first100(text):
    # strip leading/trailing spaces
    return text[:100]

for k, v in contents.items():
    print(k, len(v), first100(v))
