### HAve the user pass in multple URL's

# Upload a public notion url with customer info and requests, upload their website, give it to the bot and witness the magic.
from dotenv import load_dotenv
import os
import warnings
from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool, DirectoryReadTool, FirecrawlScrapeWebsiteTool, BaseTool, tool
from crewai.process import Process
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from textwrap import wrap
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
# from anthropic import AnthropicLLM
inp = input("What website would you like scraped and processed?: ")


load_dotenv()

# COGNITO Example:
# data = {"contigou_features": "AI Features Cognito wants: Personalised learning journey: AI will suggest the best activities to do (e.g., which lesson, quiz, FC deck, etc.), and the plan will update as students complete activities and answer questions correctly or incorrectly. Students can enter information such as dates and topics of a particular mock, and the AI plan will adapt accordingly. Adaptive learning streams: AI will update lessons, quizzes, etc., based on student performance. For example, if a student answers a question on the definition of osmosis incorrectly, they’ll be given a similar question later in the lesson, but with slight variations (e.g., different missing words). Chatbot / AI tutor: A chatbot that can answer specific questions about the course (e.g., what is the definition of diffusion), ideally pulling content from our content library rather than being entirely bespoke. 1 Marking longer Qs (automated marking): AI could mark longer written questions, suggesting which marks the student earned and providing bespoke feedback on how they could improve or clarifying their misunderstandings. AI content creation: We already use GPT-4 and Claude to generate revision notes, questions, and flashcards, and we aim to enhance this process to improve quality and reduce the manual input required from our content writers",
#          "url2": "Background info: 4th Nov 2023. Reading time: 10 min The idea of this page is to give you some background to Cognito and our users. Let me know if there is anything else that could be helpful. Cognito past, present and future (link) The above link is an overview of what we've done so far, and our future plans. It was written for new employees to understand what we're up to. --- ### Problem & value proposition Problem Students have to learn a lot of material and take exams. They have to use a variety of mediocre resources in order to get by. Value proposition Cognito provides an all in one solution that takes students from learning new material all the way to being exam ready for all 3 sciences. Cognito resources are more efficient, more engaging, comprehensive. --- ### Difficulties students face in finding resources - There is an abundance of resources for students to choose between, but most of them are: - Poorly written - Not comprehensive - Behind a paywall - Boring - It is hard for students to find resources that are specific to their: - Course (e.g. Biology AQA, Triple, Higher Tier) - This is particularly problematic as students often end up using the wrong materials and learning things they don't need to know, while missing out on things they do need to know. To give a sense of this, there are are 20-30 different GCSE biology courses. - Subject (e.g. Biology or chemistry) - Level (e.g. GCSE or A-level) - Student require a number of different resources for each stage of their learning journey: - Learning - textbooks, videos, classes - Revision/practise - revision guides, flashcards, question books - Exam technique - not really taught, indirectly from exam paper answers - Exam prep - past exam papers - Overall, students end up using a variety of resources of varying quality. As a result there is no central resource where they can visualise their courses and their current progress. The resources they use also aren't consistent with each other, personalised, or utilising any kind of gamification. - Having to navigate between so many different resources creates a lot of friction and saps motivation as they aren't really sure if they're doing it right. --- ### Target audience - Students - primary target is high schools students (currently 14-16, but soon to be 11-18) - Teachers - secondary target is teachers as they use cognito in the classroom and spread it to students - Parents - parents are only an audience in so far as they will generally be the ones paying --- ### User journey 1. Discovery Phase: - A GCSE student stumbles upon Cognito through a YouTube video, peer recommendation, their teacher's suggestion, or an online search. 2. Trial Usage: - They explore the platform's free resources, recognising their value for GCSE revision but are unable to save their progress. 3. Sign-Up: - To overcome this, the student registers for a free account, which allows progress tracking. 4. Encountering Limits: - As the student delves deeper into their revision, they reach the limit of flashcards, quiz, or exam questions offered in the free tier. 5. Committing to Pro: - Realising the benefits of unlimited flashcards and advanced features, the student opts for a Pro subscription to fully support their GCSE exam preparation. ### Sample user persona (and journey) - Student ### User Persona: Alex Demographics: - Age: 15 - Occupation: Year 11 Student - Location: London, UK - Education: Currently in GCSE study year Psychographics: - Motivated to perform well in his GCSEs and secure a place in a reputable sixth form. - Enjoys learning through interactive and visual means due to a kinetic and visual learning style. - Values a platform that can track his progress and highlight areas that need improvement. Goals: - To find a reliable and effective revision resource for his upcoming GCSE science exams. - To enhance his understanding of complex science topics through engaging, visual content. Challenges: - Struggles with traditional revision methods, like reading textbooks or making notes. - Wants to make the most efficient use of his revision time with a structured, engaging platform. Technology Usage: - Comfortable using online platforms, apps, and social media. - Frequently uses YouTube for both entertainment and educational content. ### User Journey: Alex's Interaction with Cognito Education 1. Awareness: - Alex discovers Cognito Education while browsing through YouTube for science revision videos for his GCSE exams. - Finds the video content engaging and easy to understand, catching his attention. Action Steps: - Watches multiple videos and takes notes. - Notices the link to Cognito's website in the video description and decides to explore further. 2. Consideration: - Alex browses through the website and finds a wealth of structured revision resources and quizzes. - Sees that he can track his progress by creating a free account. Action Steps: - Creates a free account to save his progress and make personalized revision more efficient. 3. Adoption (Usage): - Alex uses the platform for revision regularly, finding the quizzes helpful to identify areas for improvement. - As he approaches the free limit of questions, he considers the benefits of the pro version. Action Steps: - Upgrades to the pro version to unlock unlimited questions and additional resources. 4. Engagement: - Alex integrates Cognito Education into his daily revision schedule, utilizing the resources for efficient and targeted revision. - Engages with the platform by taking quizzes, watching videos, and reviewing modules on various science topics. Action Steps: - Sets aside specific times for using Cognito as part of his revision timetable. - Utilizes feedback and progress tracking to focus on weaker areas. 5. Advocacy: - Alex finds his revision more fruitful and feels better prepared for his exams. - He recommends Cognito Education to his friends, sharing it in their study group. Action Steps: - Shares his positive experiences and progress with friends. - Recommends Cognito Education to his study group and through his social media, helping others in their revision journey. ### Sample user persona - Teacher ### The Proactive Teacher - Name: Mr. Anderson - Age: 42 - Background: Has been teaching science for 15 years, always looking for innovative ways to engage his students. - Goals: To make science accessible and fun for all of his students. - Pain Points: Needs varied resources to cater to the diverse learning styles in his classroom. - How they found Cognito: Through an online search for specific science teaching resources. - Usage Pattern: Integrates resources into his lesson plans regularly. - Preferences: Comprehensive, curriculum-aligned, and easily-digestible materials. ### Sample user persona - Parent ### Persona 3: The Supportive Parent - Name: Mrs. Patel - Age: 38 - Background: Works full-time and has two children, seeks supplementary education materials for her kids. - Goals: To provide extra help for her children in their studies. - Pain Points: Limited time to assist with her children's studies due to work commitments. - How they found Cognito: Via an online search for science revision materials. - Usage Pattern: Sits down with her children over the weekend to explore the resources. - Preferences: Resources that are easy for parents to understand and explain to their children. --- ### Demographics - Age: Typically 14-16 years old. - Location: Mainly UK, but across the world (especially places that teach international UK courses e.g. Middle East, Singapore, HK etc). We want to expand more internationally. - Google analytics Show Image - Socioeconomic Status: Varied across the entire spectrum, but mainly students in developed nations. --- ### Behavioural aspects - Daily Usage Patterns: Highest in the evenings. Lowest Friday/Saturday. - Annual Usage Patterns: Steady Sep-Dec, rises slowly from Jan-April, big peak May/June, low July/Aug. Low during holidays like Christmas. - Purchase Motivations: Want to access more content to be able to use Cognito fully to prepare for their exam - hinges largely on them wanting to use the non-free content (i.e. FCs, Quiz, Exam Qs) - Brand Loyalty: I think we have quite a bit of brand loyalty, especially on YT and by teachers. If we made the platform better overall, we could certainly become sticky across a students whole high school years and across entire classrooms. - Trustpilot - YouTube - to see comments --- ### Technology - Device type: 25% mobile, 72% desktop, 3% mobile. - Browser: 50% Chrome, 35% Safari, 11% Edge, 2% Opera, 2% Samsung, minimal Firefox etc - Device: 41% Windows, 28% Mac, 28% iOS, 12% Chrome OS, 8% Android, minimal Linux etc We know our mobile experience is not as good as our desktop experience, so mobile share may grow if we improve mobile, especially if we develop an app. --- ### Marketing - YouTube - We have a 550k subscriber YouTube channel that gets 30M views a year. - We mention our learning platform in some videos (but only the minority/newer ones), on the rest we only have it in the comments/description. A lot of people use our YT channel and have no idea that we have a learning platform. - Geography from YT - just compare the relative %, not absolute Show Image - Views across year from YT Show Image - Word of mouth - This is the main one along with YouTube. Cognito is shared among students and teachers - often shared across whole classes or schools at a time. - FB/IG - we had FB and IG accounts, but stopped using them as they didn't seem to do much. - No paid ads - No TikTok - Poor SEO overall - No articles specifically to generate traffic"}
# user_query = "I run an AI development studio. My client, is a UK education company called Cognito. Your goal is to write up a tecnical proposal for Cognito according to the provided features they've specified. Upon recieving the data you need to first create a plan for the proposal. In the second itteration you need expand on it, and then append it to a pdf. I've attached the data of both the background info on the client - Cognito, as well as the features they are expecting. You should create 6 pages detailing: 1. **The Brief** a 400 word paragraph detailing what the project is aiming to accomplish, 2. **Scope of work** 300 words of points with sub-points detailing how we would approach the project, 3. **Feature Summary and Timeline** explaining stages of feature development and their dev time, 4. **Required Team** a markdown tree graph of the required team 5. **Per-Feature Cost** a table detailing the cost of each feature with the time in hours it will take to develop. 6.**Technical Recomendation** 400 words paragraph detailing the stack which we recommend for this project and why. After you are done check if its the correct size before uploading it."

# CONTIGOU Example:
# data = {"contigou_features": "# Contigou Feature Request ## 1. Search and Filtering Enhancements - Implement radius-based search (e.g., within X miles of city/zip code) - Add advanced filtering options: - Therapy type - Bed availability - Amenities - Future consideration: Display cost information ## 2. Map and List View Integration - Synchronize facility list and map view for consistent information - Note: Current development team to complete; if not, add to future sprint ## 3. Booking and Scheduling System - Develop appointment scheduling feature with availability display - Consider implementing block scheduling - Note: Prioritize for phase after initial user acquisition - Action item: Determine pricing strategy ## 4. Advertising and Premium Features - Create prominent featured listings to incentivize purchases - Enhance dashboard for improved data collection and analysis - Upgrade business profiles for both free and premium users ## 5. Tiered Pricing Structure Propose three-tier system (subject to revision): 1. Free (Basic) 2. Standard (Paid) 3. Premium ## 6. Customer Support Integration - Designate Renee's team as primary point of contact between users and locations - Integrate this support structure into the dashboard ## 7. Development Priorities - Focus on keeping costs low at this stage - Goal: Attract initial users and secure venture capital funding ## Next Steps - Review and provide feedback on proposed features - Finalize feature prioritization and development roadmap.",
#          "call_transcript": "# Contigou is a healthcare facility search platform ## Service Overview: The platform connects patients with skilled nursing and rehabilitation facilities, serving patients/families seeking care and healthcare facilities advertising services. ## Key Components 1. **Patient-facing site:** - Search for skilled nursing and rehab facilities - City/zip code search - Map and list views (not properly synchronized) - Basic facility information and inquiry option 2. **Business-facing site:** - Healthcare facilities create and manage profiles - Tiered subscription plans (Free, Basic, Premium) - Dashboard for managing inquiries and profile information 3. **Admin panel:** - For platform managers to oversee operations - Currently experiencing connection issues ## Current Technology Stack - Frontend: React with Next.js - Backend: Node.js - Database: Partial MongoDB implementation - Payment: Stripe API ## Desired Improvements and Features 1. **Search and Filtering:** - Radius-based search (city/zip code and distance) - More filtering options (therapy types, bed availability, amenities) - Improved search speed and efficiency - Synchronized map and list views 2. **Appointment Scheduling:** - Block scheduling system - Availability status for facilities - Potential integration with facilities' existing systems 3. **Inquiry System Enhancement:** - Improve email-based inquiry system - Two-way communication functionality - Display inquiry status to users - Consider routing inquiries through the platform 4. **User Interface and Experience:** - Modern, user-friendly redesign - Simplified language and increased font size - Improved featured facilities layout - Space for paid advertisements 5. **Business Features:** - Tiered subscription plans with varying features - Enhanced profile customization - Improved dashboard functionality - Business advertising options 6. **Data Management:** - Migration to dynamic database solution - Real-time or frequent data updates 7. **Monetization Strategies:** - Featured listings for premium subscribers - Paid advertisement spaces - Potential embeddable search for hospital websites 8. **Admin Functionality:** - Improved admin panel - Features to approve/reject new facility listings ## Development Considerations - Focus on MVP features initially - Prioritize core functionality improvements - Consider budget constraints for UI/UX redesign - Ensure scalability for future features ## Goal Create a robust, user-friendly platform serving patients and healthcare facilities while improving monetization potential."}
# user_query = "I run an AI development studio. My client, is a US healthcare facility search platform called Contigou. Your goal is to write up a tecnical proposal for Contigou according to the requested features they've specified. Upon recieving the data you need to first create a plan for the proposal. In the second itteration you need expand on it, and then append it to a pdf. I've attached the data of both the background info on the client from our past calls sumarry, as well as the features they are expecting. You should create 6 pages detailing: 1. **The Brief** a 400 word paragraph detailing what the project is aiming to accomplish, 2. **Scope of work** 300 words of points with sub-points detailing how we would approach the project, 3. **Feature Summary and Timeline** explaining stages of feature development and their dev time, 4. **Required Team** a markdown tree graph of the required team 5. **Per-Feature Cost** a table detailing the cost of each feature with the time in hours it will take to develop. 6.**Technical Recomendation** 400 words paragraph detailing the stack which we recommend for this project and why. After you are done check if its the correct size before uploading it."
import time
user_query = "Scrape the following website and add its entries to my existing shoes csv data: https://www.amazon.co.uk/shoes/s?k=shoes"
scraped_web_data = "PUMA Unisex's Smash V2 Trainers 4.5 out of 5 stars 40,869 300+ bought in past month £29.99 RRP: £52.00 FREE delivery Sat, 27 Jul for Prime members Prime Try Before You Buy 1 sustainability feature Add to basket Best Seller Skechers Men's Status 2.0 Pexton Boat Shoes Skechers Men's Status 2.0 Pexton Boat Shoes 4.6 out of 5 stars 2,656 200+ bought in past month £37.19 One-Day FREE delivery Tomorrow, 24 Jul Prime Try Before You Buy Add to basket SALOMON Men's Speedcross Trail Running Shoes +5 colours/patterns SALOMON Men's Speedcross Trail Running Shoes 4.4 out of 5 stars 8,405 £116.46 RRP: £135.00 One-Day FREE delivery Tomorrow, 24 Jul Prime Try Before You Buy Add to basket 4+ Star Styles Shop coveted styles with many reviews Sponsored Ad – Damyuan Mens Running Walking Tennis Trainers Casual Gym Athletic Fitness Sport Shoes Fashion Sneakers Ligth... +8 colours/patterns Sponsored Damyuan Mens Running Walking Tennis Trainers Casual Gym Athletic Fitness Sport Shoes Fashion Sneakers Ligthweight Comfortable Working Outdoor Flat Shoes for Jogging 4.0 out of 5 stars 14,409 50+ bought in past month £30.99 Save 20% with voucher (limited sizes/colours) One-Day FREE delivery Tomorrow, 24 Jul Mens Extra Wide Fit Trainers Walking Shoes Comfortable Running Sneakers for Flat Feet Plantar Fasciitis - Rebound Core FitVille Mens Extra Wide Fit Trainers Walking Shoes Comfortable Running Sneakers for Flat Feet Plantar Fasciitis - Rebound Core 4.4 out of 5 stars 9,704 £64.99 Save 20% with voucher (limited sizes/colours) One-Day FREE delivery Tomorrow, 24 Jul DREAM PAIRS Women's Ballet Flats Pumps Ballerina Ankle Strap Elastic Low Wedge Sandals Round Toe Comfy Dolly Shoes +3 DREAM PAIRS Women's Ballet Flats Pumps Ballerina Ankle Strap Elastic Low Wedge Sandals Round Toe Comfy Dolly Shoes 4.2 out of 5 stars 17,522 £26.99 RRP: £27.99 One-Day FREE delivery Tomorrow, 24 Jul HKR Women Trainers Athletic Running Shoes Sport Walking Sneakers Lightweight Tennis Shoes +3 HKR Women Trainers Athletic Running Shoes Sport Walking Sneakers Lightweight Tennis Shoes 4.2 out of 5 stars 17,158 £34.89 One-Day FREE delivery Tomorrow, 24 Jul STQ Womens Walking Shoes Slip-on Lightweight Mesh Sneakers Breathable Tennis Comfortable Platform Wedge Shoes +9 STQ Womens Walking Shoes Slip-on Lightweight Mesh Sneakers Breathable Tennis Comfortable Platform Wedge Shoes 4.1 out of 5 stars 13,648 £31.88 Save 10% with voucher (limited sizes/colours) One-Day FREE delivery Tomorrow, 24 Jul HKR Womens Slip on Trainers Comforble Walking Shoes with Memory Foam +7 HKR Womens Slip on Trainers Comforble Walking Shoes with Memory Foam 4.4 out of 5 stars 11,059 50+ bought in past month £33.98 One-Day FREE delivery Tomorrow, 24 Jul Baby Shoes with Soft Sole - Baby Girl Shoes - Baby Boy Shoes - Leather Toddler Shoes - Baby Walking Shoes +57 Juicy Bumbles Baby Shoes with Soft Sole - Baby Girl Shoes - Baby Boy Shoes - Leather Toddler Shoes - Baby Walking Shoes 4.4 out of 5 stars 18,022 £12.99 FREE delivery for Prime members 1 sustainability feature Small Business TIOSEBON Women Trainers Athletic Slip On Lightweight Walking Shoes - Breathable Running Sneakers +25 TIOSEBON Women Trainers Athletic Slip On Lightweight Walking Shoes - Breathable Running Sneakers 4.4 out of 5 stars 16,031 £33.88 One-Day FREE delivery Tomorrow, 24 Jul More results Hotter Women's Gravity II Lace Up Trainers Leather Lace Up Adult Active Shoes Casual Shoe Sneakers Hotter Women's Gravity II Lace Up Trainers Leather Lace Up Adult Active Shoes Casual Shoe Sneakers 3.1 out of 5 stars 2 £71.20 One-Day FREE delivery Tomorrow, 24 Jul Prime Try Before You Buy Add to basket Merrell Men's Moab 3 GTX Hiking Shoe +3 Merrell Men's Moab 3 GTX Hiking Shoe 4.4 out of 5 stars 1,190 50+ bought in past month £86.36 RRP: £135.00 One-Day FREE delivery Tomorrow, 24 Jul Prime Try Before You Buy Add to basket Vans Men's Atwood Sneaker +21 Vans Men's Atwood Sneaker 4.6 out of 5 stars 34,999 50+ bought in past month £44.00 One-Day FREE delivery Tomorrow, 24 Jul Prime Try Before You Buy Add to basket Superga Unisex's Cotu Classic Trainers +66 Superga Unisex's Cotu Classic Trainers 4.5 out of 5 stars 25,454 50+ bought in past month £25.00 RRP: £50.00 FREE delivery Sat, 27 Jul for Prime members Prime Try Before You Buy Add to basket Hush Puppies Men's Brandon Oxford Hush Puppies Men's Brandon Oxford 4.3 out of 5 stars 99 £53.37 RRP: £75.00 One-Day FREE delivery Tomorrow, 24 Jul Prime Try Before You Buy Add to basket TEEZY No Tie Shoe Laces for Trainers | Premium Elastic Weave & Quick Lock Buckle | Flat Shoe Laces For Adults & Kids | Ela... Sponsored TEEZY No Tie Shoe Laces for Trainers | Premium Elastic Weave & Quick Lock Buckle | Flat Shoe Laces For Adults & Kids | Elastic Shoelaces Black White Laces No Tie | ORIGINAL 4.2 out of 5 stars 77 £7.49 RRP: £7.99 One-Day FREE delivery Tomorrow, 24 Jul More results SALOMON Men's Xa Pro 3D Gore-tex Trail Running Shoes SALOMON Men's Xa Pro 3D Gore-tex Trail Running Shoes 4.3 out of 5 stars 9,018 £134.32 RRP: £160.00 One-Day FREE delivery Tomorrow, 24 Jul Prime Try Before You Buy Add to basket Lunar St Ives Leather Plimsoll +10 Lunar St Ives Leather Plimsoll 4.5 out of 5 stars 2,097 100+ bought in past month £39.99 RRP: £44.99 One-Day FREE delivery Tomorrow, 24 Jul Small Business Add to basket Rocket Dog Jazzin Malden Womens Multi Canvas +24 Rocket Dog Jazzin Malden Womens Multi Canvas 4.6 out of 5 stars 6,422 100+ bought in past month £14.99 Was: £19.99 One-Day FREE delivery Tomorrow, 24 Jul Prime Try Before You Buy Add to basket Feethit Trainers Men Running Shoes Tennis Sports Training Walking Gym Athletic Fitness Fashion Sneakers Trainers for Men B... +4 Feethit Trainers Men Running Shoes Tennis Sports Training Walking Gym Athletic Fitness Fashion Sneakers Trainers for Men Breathable Lightweight Comfortable Outdoor Flat Shoes for Jogging 4.4 out of 5 stars 8,654 50+ bought in past month £31.99 One-Day FREE delivery Tomorrow, 24 Jul Add to basket Women Leather Flat Loafer Ladies Casual Comfy Slider Low Wedge Heel Work Shoes +20 Jo & Joe Women Leather Flat Loafer Ladies Casual Comfy Slider Low Wedge Heel Work Shoes 4.4 out of 5 stars 3,159 £22.99 One-Day FREE delivery Tomorrow, 24 Jul Add to basket Skechers Men's Status 2.0-Lorano Boat Shoes Skechers Men's Status 2.0-Lorano Boat Shoes 4.6 out of 5 stars 5,115 100+ bought in past month £39.99 One-Day FREE delivery Tomorrow, 24 Jul Add to basket Best Seller Bruno Marc Mens Oxfords Shoes Men's Lace-ups Formal Dress Shoes for Men DREAM PAIRS Bruno Marc Mens Oxfords Shoes Men's Lace-ups Formal Dress Shoes for Men 4.3 out of 5 stars 20,498 £33.99 One-Day FREE delivery Tomorrow, 24 Jul Prime Try Before You Buy Add to basket Tommy Hilfiger - Harlow Low Top Sneakers for Men - Shoes for Men UK, Mens Shoes, Mens, Walking Shoes Mens, Shoes - Trainers +3 Tommy Hilfiger Harlow Low Top Sneakers for Men - Shoes for Men UK, Mens Shoes, Mens, Walking Shoes Mens, Shoes - Trainers 4.3 out of 5 stars 17,495 50+ bought in past month £48.00 RRP: £65.00 One-Day FREE delivery Tomorrow, 24 Jul Prime Try Before You Buy Add to basket Best Seller TOMS Men's Recycled Cotton Alpargata Loafer Flat TOMS Men's Recycled Cotton Alpargata Loafer Flat 4.5 out of 5 stars 2,686 400+ bought in past month £26.40 RRP: £44.00 One-Day FREE delivery Tomorrow, 24 Jul Prime Try Before You Buy Add to basket Clarks Men's Step Urban Mix Sneaker Clarks Men's Step Urban Mix Sneaker 4.3 out of 5 stars 4,261 £42.73 One-Day FREE delivery Tomorrow, 24 Jul Add to basket Merrell Men's Jungle Moc Ltr Sr-Black +10 Merrell Men's Jungle Moc Ltr Sr-Black 4.6 out of 5 stars 23,401 £87.17 RRP: £110.00 One-Day FREE delivery Tomorrow, 24 Jul Prime Try Before You Buy See options"

# Initialize tools
file_read_tool = FileReadTool(file = '/Users/gleb/Desktop/CS/Projects/Event/Data_engineer_agent/Shoes.csv')
directory_read_tool = DirectoryReadTool(directory='/Users/gleb/Desktop/CS/Projects/Event/Data_engineer_agent')
# firecrawl_tool = FirecrawlScrapeWebsiteTool()

###### ------------ TOOLS ------------  #######
@tool("CSV upload tool")
def csv_tool(data: str, file_path: str) -> str:
    """A tool for appending data to the CSV file. Should be used last, after all the columns of the csv have been identified, and data formated. Args: data: Data that needs uploading to the csv file, file_path: Path to the CSV file as a string"""
    with open(file_path, 'a') as file:
        file.write(data)
    return "Data appended to CSV successfully!"

@tool("PDF creation tool")
def create_pdf(data: str, file_path: str) -> str:
    "A tool for turning text into a PDF. Args: data: String of data that needs to be converted to PDF, file_path: Path where to save the PDF file"
    
    # Create the PDF object
    c = canvas.Canvas(file_path, pagesize=letter)
    
    # Register a default font (you may need to adjust the path)
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    c.setFont('Arial', 12)
    
    # Get page width and set margins
    page_width, page_height = letter
    left_margin = 40
    right_margin = 40
    top_margin = 50
    bottom_margin = 50
    line_height = 15
    
    # Calculate maximum width for text
    max_width = page_width - left_margin - right_margin
    
    # Split the data into lines
    lines = data.split('\n')
    
    y = page_height - top_margin  # Start near the top of the page
    
    for line in lines:
        # Check if the line is part of a table (you may need to adjust this condition)
        if '\t' in line or '|' in line:
            # It's a table row, draw it as is
            c.drawString(left_margin, y, line)
            y -= line_height
        else:
            # It's regular text, wrap it
            wrapped_lines = simpleSplit(line, 'Arial', 12, max_width)
            for wrapped_line in wrapped_lines:
                c.drawString(left_margin, y, wrapped_line)
                y -= line_height
        
        # Check if we need a new page
        if y < bottom_margin:
            c.showPage()
            c.setFont('Arial', 12)
            y = page_height - top_margin
    
    # Save the PDF
    c.save()
    return f"PDF created successfully at {file_path}"

# Set environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4-turbo'


### --- SCRAPING AGENT --- ###
scraper_agent = Agent(
    role="Web Scrapper agent",
    goal="Scroll given websites based on the URL, URLs or data provided by the user and return the contents to the next agent.",
    backstory="You're an AI agent scraping the web.",
    tools=[],
    allow_delegation=False,
    verbose=True,
)

data_scraping = Task(
    description=f"""user_query = {user_query}, scraped_web_data = {scraped_web_data}\n
    1. Upon extracting the data, based on the user query filter and format it to suit the user request. As an example The user_query might require to scrape a website, and upload the product data to a csv, in which case after scraping it you'd need to distinctly structure it in a table. Alternatively the query might require you to clean/select/structure/summarize the data.
    2. Pass the processed data to the next agent.\n""",
    expected_output="Processed and upploaded data according to the user query",
    agent=scraper_agent
)

### --- DATA UPLOADING AGENT --- ###
proccessing_agent = Agent(
    role="Data managing agent",
    goal="Format and export the data into a relevenat document based on the user query.",
    backstory="You're an AI agent helping a user by formating and exporting data.",
    tools=[directory_read_tool, file_read_tool, csv_tool, create_pdf],
    allow_delegation=False,
    verbose=True,
    max_execution_time=None,
)

# !!! DELETED LINE FOR CONTIGO U PROPOSAL EXAMPLE !!! #
# 1. Upon receiving the data from the previouse agent, according to the user query, format the data to fit the task and the document it will be uploaded to.
# 4. If the query requires you to upload the data to an existing file/database, make sure you read the file first to confirm it's structure, and then format the data accordingly before adding it to the file.""",

data_processing = Task(
    description=f"""user_query= {user_query}, scraped_web_data = {scraped_web_data}\n
    0. Based on the user_query find the right file or where the file should be created. Then follow these stpes in the precise order:\n
    1. Based on the user_query, if you are creating a PDF:, draft a proposal structure, outlining what the key sections will be whilst adhearing to the structural requirements specified in the user_query.\n
        - 1.1 After drafting the proposal use the draft to expand the plan into a full proposal, adhearing to the requested length in the user_request.\n
        - 1.2 Export that data using a pdf tool.\n
    2. If you are asked to deal with a csv:\n
        - 2.1 Read the file to identify the structure of the collumns and the format of the entries.\n 
        2.2 Structure the data according to the csv collumns, UNDER NO CIRCUMSTANCE LEAVE OUT ANY ENTRIES use the entire scraped_web_data.
        - 2.3 Upload the data to the csv. Do not leave out any entries!
        - 2.4 Confirm the uploaded fields are correct and no entries were missplaced. For instance, the name of the product shouldnt be in the delivery date. THIS IS THE MOST IMPORTANT STEP!!!. Take an extra action to crosscheck if the CSV entries are missplaced. If they are, correct them.""",
    expected_output="Processed data according to the user query",
    agent=proccessing_agent
)
time.sleep(2)

# scraper_agent
# data_scraping
crew = Crew(
    agents=[proccessing_agent],
    tasks=[data_processing],
    verbose=2,
    process=Process.sequential
)
time.sleep(2)
result = crew.kickoff()


# class CSV_Tool(BaseTool):
#     name: str = "CSV upload tool"
#     description: str = "A tool for appending data to the CSV file. It takes in two arguments: 1.Data that needs uploading to the csv file, 2.Path to the CSV file as a string."

#     def _run(self, data, file_path: str) -> str:
#         with open(file_path, 'a') as file:
#             file.write(result)
#             print("data appended to csv successfully!")


    

