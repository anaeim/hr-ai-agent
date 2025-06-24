from typing import List
from datetime import datetime

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI

def get_present_date():
    now = datetime.now()
    month_name = now.strftime("%B")
    current_year = now.year
    return f"Month: {month_name}, Year: {current_year}"

class SkillSummary(BaseModel):
    """Structured output for skill summary with key experiences and corresponding months of experience."""
    
    skill_name: str = Field(
        description="The specific skill being summarized"
    )
    
    summary: str = Field(
        description="Concise 3-5 sentence summary highlighting key experience, projects, and achievements related to the skill"
    )
    
    key_experiences: List[str] = Field(
        description="List of 2-4 most relevant experiences, projects, or accomplishments demonstrating the skill",
        max_items=4
    )
    
    months_of_experience: List[int] = Field(
        description="Months of experience for each corresponding key experience (same order as key_experiences). If not determinable, use 0 for that item",
    )


llm = ChatOpenAI(model="gpt-4o", temperature=0)
structured_llm_summary_writer = llm.with_structured_output(SkillSummary)


system_prompt = """You are an expert resume analyzer specializing in skill assessment and summarization.

Your task is to analyze resume content and create a comprehensive summary for a specific skill.

Current Date: {current_date}

Guidelines:
1. Focus on concrete examples, quantifiable achievements, and specific projects
2. Extract the most relevant and impressive experiences that showcase the skill
3. For each key experience, determine the months of experience associated with it
4. The months_of_experience list must have the same length as key_experiences list
5. If months of experience cannot be determined for a specific experience, use 0
6. Be precise about matching each experience with its corresponding duration in months
7. Convert any duration information (years, date ranges) to total months
8. When you see "Present", "Current", or similar terms in date ranges, calculate duration up to the current date provided above
9. Handle date ranges properly: if an experience shows "Jan 2022 - Present", calculate months from Jan 2022 to the current date

Important: Ensure that key_experiences and months_of_experience lists are exactly the same size, with each months_of_experience item corresponding to the same index in key_experiences.

Date Calculation Examples:
- "Jan 2022 - Present" (if current date is June 2025) = 42 months
- "2023 - Current" (if current date is June 2025) = approximately 18 months
- "Mar 2024 - Present" (if current date is June 2025) = 15 months

Output a structured summary that would be valuable for recruiters and hiring managers."""

user_prompt = """Analyze the following resume content for the specified skill:

DESIRED SKILL: {desired_skill}

RESUME CONTENT:
{resume_content}

Please provide a comprehensive skill summary following the structured format. 

Remember: 
- Extract key experiences that demonstrate the skill
- For each key experience, provide the corresponding months of experience as an integer
- Convert any date ranges or years to total months (e.g., 2 years = 24 months)
- Ensure both lists have the same number of items"""


fine_grained_skill_grader_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", user_prompt)
])


fine_grained_skill_grader: RunnableSequence = fine_grained_skill_grader_prompt | structured_llm_summary_writer