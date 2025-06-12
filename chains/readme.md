# Save the README content as a markdown file

readme_content = """
# 🧠 AgentAI - HR Application Assistant

## Overview

**AgentAI** is an intelligent HR Agent built to streamline and enhance the recruitment process. Designed specifically for modern HR departments struggling with high volumes of job applications, AgentAI leverages advanced AI models to **automatically parse resumes**, **evaluate candidate skills**, and **generate ranked shortlists**—making hiring **faster, fairer, and more accurate**.

This Jupyter-based application integrates cutting-edge Vision-Language and Large Language Models to understand resume layouts, grade skill presence, generate structured skill summaries, and rerank top candidates.

---

## 🚨 The Problem

Recruiters face:
- **Thousands of resumes** per job post
- **Manual screening bottlenecks**
- **Missed top talent** due to information overload
- **Bias and inconsistency** in evaluation

---

## ✅ The Solution

AgentAI addresses these challenges with an **end-to-end AI-powered workflow** that:
- Extracts and understands resume content from PDFs
- Evaluates whether key job-specific skills are present
- Generates human-readable skill summaries with proficiency assessments
- Reranks selected resumes against a strong applicant profile

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
