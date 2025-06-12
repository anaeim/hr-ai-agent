from typing import List, Optional

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI

class SkillSummary(BaseModel):
    """Structured output for skill summary with enhanced fields."""
    
    skill_name: str = Field(
        description="The specific skill being summarized"
    )
    
    proficiency_level: str = Field(
        description="Assessed proficiency level (Beginner, Intermediate, Advanced, Expert)"
    )
    
    summary: str = Field(
        description="Concise 3-5 sentence summary highlighting key experience, projects, and achievements related to the skill"
    )
    
    key_experiences: List[str] = Field(
        description="List of 2-4 most relevant experiences, projects, or accomplishments demonstrating the skill",
        max_items=4
    )
    
    years_of_experience: Optional[str] = Field(
        description="Estimated years of experience with this skill (if determinable from resume; otherwise, write 'NOT GIVEN'",
        default=None
    )
    
    confidence_score: float = Field(
        description="Confidence score (0.0-1.0) indicating how well the skill is demonstrated in the resume",
        ge=0.0,
        le=1.0
    )



llm = ChatOpenAI(model="gpt-4o", temperature=0)
structured_llm_summary_writer = llm.with_structured_output(SkillSummary)



system_prompt = """You are an expert resume analyzer specializing in skill assessment and summarization.

Your task is to analyze resume content and create a comprehensive summary for a specific skill.

Guidelines:
1. Focus on concrete examples, quantifiable achievements, and specific projects
2. Assess proficiency level based on:
   - Complexity of projects/responsibilities
   - Leadership roles or mentoring others
   - Years of experience
   - Depth of technical knowledge demonstrated
3. Extract the most relevant and impressive experiences that showcase the skill
4. Provide an honest confidence score based on how well the skill is demonstrated
5. If the skill is not well-represented in the resume, be honest about limited evidence

Proficiency Levels:
- Beginner: Basic knowledge, limited practical experience
- Intermediate: Solid foundation with practical application in projects
- Advanced: Extensive experience, complex projects, possible leadership
- Expert: Deep expertise, innovation, teaching/mentoring others, industry recognition

Output a structured summary that would be valuable for recruiters and hiring managers."""

user_prompt = """Analyze the following resume content for the specified skill:

DESIRED SKILL: {desired_skill}

RESUME CONTENT:
{resume_content}

Please provide a comprehensive skill summary following the structured format."""


summary_writer_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", user_prompt)
])



skill_summary_writer: RunnableSequence = summary_writer_prompt | structured_llm_summary_writer