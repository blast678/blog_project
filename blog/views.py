from django.shortcuts import render

blogs = {
    "Artificial Intelligence": "Artificial Intelligence (AI) refers to machines that can perform tasks that typically require human intelligence, such as learning, reasoning, and problem-solving. It is transforming industries like healthcare, finance, and education by automating complex processes and providing valuable insights.",
    
    "Sustainable Living": "Sustainable living encourages individuals to reduce their environmental impact by making conscious lifestyle choices. This includes using renewable energy, minimizing waste, adopting plant-based diets, and supporting eco-friendly products to help protect the planet for future generations.",
    
    "Remote Work": "Remote work has gained immense popularity, allowing employees to work from anywhere with an internet connection. It offers flexibility and better work-life balance but also requires strong communication skills and self-discipline to stay productive and connected with teams.",
    
    "Mental Health Awareness": "Mental health awareness emphasizes understanding and addressing emotional and psychological well-being. Open conversations, access to resources, and reducing stigma are crucial to help people seek support and lead healthier lives.",
    
    "Blockchain Technology": "Blockchain technology provides a decentralized and secure way to record transactions and share data. It is best known as the foundation of cryptocurrencies like Bitcoin, but it is also being explored for supply chain management, voting systems, and digital identity verification.",
    
    "Space Exploration": "Space exploration pushes the boundaries of human knowledge and technology as we study planets, stars, and the universe beyond Earth. Missions to Mars and advancements in satellite technology continue to inspire curiosity and innovation worldwide.",
    
    "Digital Marketing": "Digital marketing involves promoting products or services using online platforms like social media, search engines, and email. It allows businesses to reach a global audience, analyze user behavior, and create highly targeted campaigns for better engagement and sales.",
    
    "Healthy Eating": "Healthy eating focuses on consuming a balanced diet rich in fruits, vegetables, whole grains, and lean proteins. It supports overall well-being, strengthens immunity, and reduces the risk of chronic diseases, empowering people to lead energetic and fulfilling lives.",
    
    "Personal Finance": "Personal finance is the practice of managing your money through budgeting, saving, investing, and planning for the future. Learning to handle finances wisely helps achieve financial independence, reduce stress, and prepare for unexpected expenses or retirement.",
    
    "Travel Blogging": "Travel blogging allows adventurers to document and share their experiences exploring different cultures, cuisines, and landscapes. It inspires others to travel, provides practical tips, and often becomes a source of income through collaborations and sponsored content."
}
def starting_page(request):
    return render(request,"blog/index.html")
#  blog=list(blogs.keys());
#     return render(request,"blog/index.html")
def posts(request):
    pass
def post_detail(request):
    pass
# Create your views here.
