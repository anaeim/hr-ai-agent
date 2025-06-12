
# 🧠 AgentAI - HR Application Assistant

## Overview

**AgentAI** is an intelligent HR Agent built to streamline and enhance the recruitment process. Designed specifically for modern HR departments struggling with high volumes of job applications, AgentAI leverages advanced AI models to **automatically parse resumes**, **evaluate candidate skills**, and **generate ranked shortlists**—making hiring **faster, fairer, and more accurate**.

This Jupyter-based application integrates cutting-edge Vision-Language and Large Language Models to understand resume layouts, grade skill presence, generate structured skill summaries, and rerank top candidates.

---

## 🚨 The Problem

Modern HR departments face an overwhelming volume of applications for every job posting, making it nearly impossible for human recruiters to efficiently review and evaluate each candidate. This results in:

- **Significant delays** in the hiring process
- **Overlooked qualified candidates**
- **Inconsistent and biased hiring decisions**

These challenges make it difficult for companies to build strong, diverse, and high-performing teams.

---

## ✅ The Solution

AgentAI is an AI-powered HR Agent designed to transform how organizations handle recruitment. It addresses these challenges by:

- **Automatically screening resumes** with layout-aware PDF understanding
- **Identifying top candidates** using job-specific skill assessment
- **Providing unbiased shortlists** through structured evaluation and reranking

This ensures a hiring process that is:
- **Faster** – drastically reducing time-to-hire
- **Fairer** – evaluating candidates objectively
- **More accurate** – matching resumes to role requirements with high precision

By removing manual bottlenecks and unconscious bias, AgentAI significantly improves the **quality and consistency** of hiring decisions.

---

## 📁 Code Structure

Implemented in a Graph-based Jupyter Notebook (`graph.ipynb`) using modular LangChain components. The system comprises four main components:

### 1. 📄 PDF Layout Understanding
- Uses **Qwen 2.5 VLM** for visually structured extraction from PDF resumes.
- Parses layout to intelligently retrieve text blocks in context.

---

### 2. 🧪 Skill Grader

- Checks if a **desired skill** is explicitly present in a resume.
- Uses a **binary scoring system** (`True`/`False`).
- Built with `LangChain`, `Pydantic`, and `GPT-4o`.

#### Chain Summary
- Input: Resume content + target skill
- Output: `True` if skill is demonstrated with evidence, `False` otherwise

```python
# True if clearly mentioned or shown in experience/projects
binary_score: bool = True | False
```

---

### 3. 📝 Skill Summary Writer

- Evaluates skill depth if the skill is found in a resume.
- Generates a **structured summary** including:
  - Proficiency level
  - Key achievements
  - Estimated years of experience
  - Confidence score

#### Output Format:
```json
{
  "skill_name": "Python",
  "proficiency_level": "Advanced",
  "summary": "...",
  "key_experiences": [...],
  "years_of_experience": "3",
  "confidence_score": 0.93
}
```

---

### 4. 📊 Resume Reranker

- Uses **Qwen3-Reranker-8B** to sort shortlisted resumes.
- Ranks resumes against an **ideal candidate profile**.
- Optimizes final selection for hiring teams.

---

## 🚀 Technologies Used

| Component            | Technology               |
|---------------------|--------------------------|
| PDF Parsing         | Qwen 2.5 VLM             |
| Skill Grading       | GPT-4o + LangChain       |
| Summary Generation  | GPT-4o + Pydantic        |
| Reranking           | Qwen3-Reranker-8B        |
| Notebook Framework  | Jupyter + LangChain Graph |

---

## 🔧 How to Use

1. Clone this repo and open `graph.ipynb`.
2. Upload resumes in PDF format.
3. Define desired skills and ideal candidate traits.
4. Run the notebook cells step-by-step.
5. View graded skills, summaries, and top-ranked candidates.

---

## 📈 Benefits

- **Save time** with automatic screening
- **Improve fairness** with objective evaluations
- **Enhance quality** of hires through structured insights
- **Support recruiters** with smart, AI-driven decisions

---

## 📬 Contact

For more information or integration support, reach out to the AgentAI team.
