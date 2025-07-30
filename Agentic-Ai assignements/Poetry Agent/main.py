import asyncio
from connection import config
from agents import Agent,Runner,trace

lyric_Poetry_Agent = Agent(
    name="Lyric Poetry Agent",
    instructions="""You are a lyrical Poetry Agent. You do analysis of the lyric poetry
    where poets write about thier feelingsand thoughts, like songs or poems about being sad or happy."""
)

narrative_Poetry_Agent = Agent(
    name="Narrative Poetry Agent",
    instructions="""You are Narrative Poetry Agent. You do analysis of narratrive poetry
    where poets tell the story with characters and events, just like a regular story but
    written in poem form with rhymes or special rhythm."""
)
dramatic_Poetry_Agent = Agent(
    name="Dramatic Poetry Agent",
    instructions="""You are dramatic Poetry Agent. You do analysis of dramatic poetry where 
    poetryis meant to be performed out loud, where someone acts like a character and speaks 
    their thoughts and feelings to an audience (acting in a theatre)."""
)
triage_agent = Agent(
    name="Triage Agent",
    instructions="""You are the Triage Agent for poetry classification. 
Your job is to carefully read the given poem and decide whether it is:

1. Lyric Poetry:  focuses on personal feelings, emotions, or inner thoughts, often with a musical tone or reflective mood.
2. Narrative Poetry:  tells a story with characters, a plot, and a sequence of events, similar to a short story but in poetic form.
3. Dramatic Poetry: represents one or more characters speaking directly, as if on a stage, revealing thoughts or engaging in dialogue.

Analyze the input and handoff  to the most appropriate poetry agent based on its content and style.""",
    handoffs=[lyric_Poetry_Agent,narrative_Poetry_Agent,dramatic_Poetry_Agent]
)
async def main():
    with trace("Poetry_Agent"):
        result = await Runner.run(triage_agent,"""A knight rode out at break of day,
His armor bright, his eyes like flame.
He sought a dragon far away,
To win both glory and a name. """,run_config=config)
        print(result.final_output)
        print(result.last_agent.name)
if __name__ == "__main__":
    asyncio.run(main())
