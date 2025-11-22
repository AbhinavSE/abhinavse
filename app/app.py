import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""
    pass


def navbar() -> rx.Component:
    """The navigation bar."""
    return rx.hstack(
        rx.link(
            rx.button("Home", variant="soft"),
            href="/",
        ),
        rx.link(
            rx.button("About", variant="soft"),
            href="/about",
        ),
        rx.spacer(),
        rx.heading("Welcome!", size="5"),
        rx.color_mode.button(margin_left="1em"),
        width="100%",
        padding="1em",
        background_color=rx.color("gray", 2),
        align="center",
    )


def index() -> rx.Component:
    """The home page."""
    return rx.vstack(
        navbar(),
        rx.container(
            rx.heading("Home", size="8", margin_bottom="1em"),
            rx.text(""),
            padding_top="2em",
        ),
        width="100%",
    )


def about() -> rx.Component:
    """The about page with resume details."""
    return rx.vstack(
        navbar(),
        rx.container(
            rx.heading("Abhinav Ennazhiyil", size="8", margin_bottom="0.2em"),
            rx.text("Data Scientist", size="5", color="gray", margin_bottom="1em"),
            
            rx.hstack(
                 rx.link(rx.icon("linkedin", size=20), href="https://linkedin.com/in/abhinav-ennazhiyil"),
                 rx.link(rx.icon("github", size=20), href="https://github.com/AbhinavSE"),
                 spacing="4",
                 margin_bottom="2em",
            ),

            rx.vstack(
                rx.heading("Profile", size="6"),
                rx.text(
                    "Data scientist with a Bachelor's degree in Computer Science and 3 years of work experience. Proven track record of building and deploying ML and LLM-based solutions that drive business impact across marketing, sales, and finance. Developed a high-performing CLTV model from scratch and designed AI systems that generate personalized marketing emails and financial reports using Retrieval-Augmented Generation (RAG) frameworks. Skilled in working cross-functionally with stakeholders to translate complex business challenges into scalable data products. Strong technical foundation in machine learning, LangChain, AWS Bedrock, and data experimentation, with a focus on delivering actionable insights and measurable outcomes.",
                    line_height="1.6",
                ),
                align_items="start",
                width="100%",
                margin_bottom="2em",
            ),

             rx.vstack(
                rx.heading("Skills", size="6"),
                rx.flex(
                    rx.badge("LangChain", variant="soft"),
                    rx.badge("PydanticAI", variant="soft"),
                    rx.badge("RAG", variant="soft"),
                    rx.badge("AWS Bedrock", variant="soft"),
                    rx.badge("Machine Learning (Regression, Classification, Clustering)", variant="soft"),
                    rx.badge("Statistical Analysis", variant="soft"),
                    rx.badge("Python", variant="soft"),
                    rx.badge("Excel", variant="soft"),
                    rx.badge("SQL", variant="soft"),
                     rx.badge("Project Management", variant="soft"),
                    spacing="2",
                    flex_wrap="wrap",
                ),
                align_items="start",
                width="100%",
                margin_bottom="2em",
            ),

            rx.vstack(
                rx.heading("Professional Experience", size="6"),
                rx.box(
                    rx.hstack(
                        rx.heading("Data Scientist", size="4"),
                        rx.spacer(),
                        rx.text("Jun 2022 – present", color="gray", size="2"),
                        width="100%",
                    ),
                     rx.text("C2FO | Noida, Delhi", size="2", weight="bold", margin_bottom="0.5em"),
                    
                    rx.text("AI Email Generator", weight="bold", size="2"),
                    rx.unordered_list(
                        rx.list_item("Built C2FO's first production-grade GenAI application, increasing average response rates from ~1% to ~5% across Europe and the U.S."),
                        rx.list_item("LLM-driven marketing email generator using LangChain and AWS Bedrock, integrated into Marketo."),
                         rx.list_item("Email personalization using real-time Internal data, conversation history, and external data like market trends, press releases, etc."),
                        rx.list_item("Implemented quality assurance using a custom validation system (DeepEval)."),
                        padding_left="1em",
                         margin_bottom="1em",
                    ),

                     rx.text("AI Financial Reports", weight="bold", size="2"),
                    rx.unordered_list(
                         rx.list_item("Developed a financial report generator to support the marketing team with customer's working capital insights, reducing research effort from ~3 days to ~2 min."),
                        rx.list_item("Used a RAG pipeline with LangChain and AWS Bedrock to extract and synthesize key trends from SEC 10-K/10-Q filings."),
                        rx.list_item("Integrated the reports into Salesforce for on-demand sales enablement."),
                         padding_left="1em",
                         margin_bottom="1em",
                    ),

                     rx.text("Customer Lifetime Value Model", weight="bold", size="2"),
                     rx.unordered_list(
                         rx.list_item("Engineered a custom Customer Lifetime Value model using XGBoost with ~70% recall."),
                         rx.list_item("Defined customer lifetime value segments using a RFM matrix for a period of 1 year from first transaction."),
                         rx.list_item("Tested the performance using a A/B Testing framework in collaboration with the campaign management team."),
                         padding_left="1em",
                          margin_bottom="1em",
                     ),
                     
                     rx.text("Trigger based sales prioritization", weight="bold", size="2"),
                     rx.unordered_list(
                         rx.list_item("Developed a custom spike‑detection logic for significant jumps in the customer's accounts payable and day sales outstanding."),
                         rx.list_item("Integrated into the sales‑targeting system to prioritize high‑impact accounts."),
                         padding_left="1em",
                     ),
                     
                    margin_bottom="1em",
                ),
                align_items="start",
                width="100%",
                margin_bottom="2em",
            ),
            
             rx.vstack(
                rx.heading("Projects", size="6"),
                rx.box(
                    rx.link(
                        rx.heading("The LLM Podcast", size="4", _hover={"color": "blue", "text_decoration": "underline"}),
                        href="https://thellmpodcast.in",
                        is_external=True,
                    ),
                     rx.text("An LLM driven sports news website", size="2", color="gray", margin_bottom="0.5em"),
                    rx.unordered_list(
                        rx.list_item("Curated real-time sports news by scraping articles from multiple online sources, leveraging LLM agents to extract and synthesize relevant insights."),
                         rx.list_item("Implemented unsupervised clustering algorithms (cosine similarity with gemini embeddings) to group similar articles, followed by LLM-based summarization."),
                        rx.list_item("Developed an automated podcast engine where two distinct LLM personas engage in dynamic, human-like dialogue."),
                        padding_left="1em",
                    ),
                    margin_bottom="1em",
                ),
                align_items="start",
                width="100%",
                margin_bottom="2em",
            ),

            rx.vstack(
                rx.heading("Education", size="6"),
                rx.box(
                    rx.hstack(
                         rx.heading("Bachelor of Technology in CSE", size="4"),
                         rx.spacer(),
                         rx.text("2018 – 2022", color="gray", size="2"),
                         width="100%",
                    ),
                    rx.text("IIIT Delhi", size="2", weight="bold"),
                    rx.text("8.4 CGPA", size="2", color="gray"),
                    margin_bottom="1em",
                ),
                align_items="start",
                width="100%",
                margin_bottom="2em",
            ),
            
            padding_top="2em",
            padding_bottom="4em",
            max_width="800px",
        ),
        width="100%",
    )


app = rx.App()
app.add_page(index)
app.add_page(about)
