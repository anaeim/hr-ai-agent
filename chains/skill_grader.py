from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)


class SkillFinder(BaseModel):
    """Binary score for a skill present in resume content"""

    binary_score: bool = Field(
        description="True if the desired skill is clearly present and supported by resume content, False otherwise"
    )


structured_llm_grader = llm.with_structured_output(SkillFinder)

system = """You are a skill grader with attention to details assessing whether a specific skill is present in a resume content.

Give a binary score True or False:
- True: The specific desired skill is explicitly mentioned OR clearly demonstrated through concrete examples, projects, or experience in the resume
- False: The skill is not mentioned, only vaguely implied, or there's insufficient evidence of the skill

Be strict in your evaluation - only return True if there's clear evidence of the skill."""

skill_finder_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Desired skill: {desired_skill}\n\nResume content: {resume_content}"),
    ]
)

skill_grader: RunnableSequence = skill_finder_prompt | structured_llm_grader