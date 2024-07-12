top_k_mappings = {}

# top_k_mappings["False_False_False_False_None"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["False_False_False_False_Combined"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 16,
# }
# top_k_mappings["False_False_False_True_None"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 16,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["False_False_False_True_Combined"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 8,
#     "search_docs_top_k": 8,
# }
# top_k_mappings["False_False_True_False_None"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 16,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["False_False_True_False_Combined"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 8,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 8,
# }
# top_k_mappings["False_False_True_True_None"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 8,
#     "search_arxiv_top_k": 8,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["False_False_True_True_Combined"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 5,
#     "search_arxiv_top_k": 5,
#     "search_docs_top_k": 6,
# }
# top_k_mappings["False_True_False_False_None"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 4,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["False_True_False_False_Combined"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 2,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 8,
# }
# top_k_mappings["False_True_False_True_None"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 2,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 8,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["False_True_False_True_Combined"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 2,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 4,
#     "search_docs_top_k": 4,
# }
# top_k_mappings["False_True_True_False_None"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 2,
#     "search_wikipedia_top_k": 8,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["False_True_True_False_Combined"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 2,
#     "search_wikipedia_top_k": 4,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 4,
# }
# top_k_mappings["False_True_True_True_None"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 2,
#     "search_wikipedia_top_k": 4,
#     "search_arxiv_top_k": 4,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["False_True_True_True_Combined"] = {
#     "search_knowledge_base_top_k": 0,
#     "search_online_top_k": 1,
#     "search_wikipedia_top_k": 4,
#     "search_arxiv_top_k": 4,
#     "search_docs_top_k": 4,
# }
# top_k_mappings["True_False_False_False_None"] = {
#     "search_knowledge_base_top_k": 16,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["True_False_False_False_Combined"] = {
#     "search_knowledge_base_top_k": 8,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 8,
# }
# top_k_mappings["True_False_False_True_None"] = {
#     "search_knowledge_base_top_k": 8,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 8,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["True_False_False_True_Combined"] = {
#     "search_knowledge_base_top_k": 5,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 5,
#     "search_docs_top_k": 6,
# }
# top_k_mappings["True_False_True_False_None"] = {
#     "search_knowledge_base_top_k": 8,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 8,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["True_False_True_False_Combined"] = {
#     "search_knowledge_base_top_k": 5,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 5,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 6,
# }
# top_k_mappings["True_False_True_True_None"] = {
#     "search_knowledge_base_top_k": 6,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 5,
#     "search_arxiv_top_k": 5,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["True_False_True_True_Combined"] = {
#     "search_knowledge_base_top_k": 4,
#     "search_online_top_k": 0,
#     "search_wikipedia_top_k": 4,
#     "search_arxiv_top_k": 4,
#     "search_docs_top_k": 4,
# }
# top_k_mappings["True_True_False_False_None"] = {
#     "search_knowledge_base_top_k": 8,
#     "search_online_top_k": 2,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["True_True_False_False_Combined"] = {
#     "search_knowledge_base_top_k": 8,
#     "search_online_top_k": 1,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 4,
# }
# top_k_mappings["True_True_False_True_None"] = {
#     "search_knowledge_base_top_k": 6,
#     "search_online_top_k": 1,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 6,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["True_True_False_True_Combined"] = {
#     "search_knowledge_base_top_k": 4,
#     "search_online_top_k": 1,
#     "search_wikipedia_top_k": 0,
#     "search_arxiv_top_k": 4,
#     "search_docs_top_k": 4,
# }
# top_k_mappings["True_True_True_False_None"] = {
#     "search_knowledge_base_top_k": 6,
#     "search_online_top_k": 1,
#     "search_wikipedia_top_k": 6,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["True_True_True_False_Combined"] = {
#     "search_knowledge_base_top_k": 4,
#     "search_online_top_k": 1,
#     "search_wikipedia_top_k": 4,
#     "search_arxiv_top_k": 0,
#     "search_docs_top_k": 4,
# }
# top_k_mappings["True_True_True_True_None"] = {
#     "search_knowledge_base_top_k": 4,
#     "search_online_top_k": 1,
#     "search_wikipedia_top_k": 4,
#     "search_arxiv_top_k": 4,
#     "search_docs_top_k": 0,
# }
# top_k_mappings["True_True_True_True_True"] = {
#     "search_knowledge_base_top_k": 3,
#     "search_online_top_k": 1,
#     "search_wikipedia_top_k": 3,
#     "search_arxiv_top_k": 3,
#     "search_docs_top_k": 3,
# }


top_k_mappings["False_False_False_False_False"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 0,
    "search_patent_top_k": 0,
    "search_edu_top_k": 0,
    "search_esg_top_k": 0,
}
top_k_mappings["False_False_False_False_True"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 0,
    "search_patent_top_k": 0,
    "search_edu_top_k": 0,
    "search_esg_top_k": 16,
}
top_k_mappings["False_False_False_True_False"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 0,
    "search_patent_top_k": 0,
    "search_edu_top_k": 16,
    "search_esg_top_k": 0,
}
top_k_mappings["False_False_False_True_True"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 0,
    "search_patent_top_k": 0,
    "search_edu_top_k": 8,
    "search_esg_top_k": 8,
}
top_k_mappings["False_False_True_False_False"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 0,
    "search_patent_top_k": 16,
    "search_edu_top_k": 0,
    "search_esg_top_k": 0,
}
top_k_mappings["False_False_True_False_True"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 0,
    "search_patent_top_k": 8,
    "search_edu_top_k": 0,
    "search_esg_top_k": 8,
}
top_k_mappings["False_False_True_True_False"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 0,
    "search_patent_top_k": 8,
    "search_edu_top_k": 8,
    "search_esg_top_k": 0,
}
top_k_mappings["False_False_True_True_True"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 0,
    "search_patent_top_k": 5,
    "search_edu_top_k": 5,
    "search_esg_top_k": 6,
}
top_k_mappings["False_True_False_False_False"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 4,
    "search_patent_top_k": 0,
    "search_edu_top_k": 0,
    "search_esg_top_k": 0,
}
top_k_mappings["False_True_False_False_True"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 2,
    "search_patent_top_k": 0,
    "search_edu_top_k": 0,
    "search_esg_top_k": 8,
}
top_k_mappings["False_True_False_True_False"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 2,
    "search_patent_top_k": 0,
    "search_edu_top_k": 8,
    "search_esg_top_k": 0,
}
top_k_mappings["False_True_False_True_True"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 2,
    "search_patent_top_k": 0,
    "search_edu_top_k": 4,
    "search_esg_top_k": 4,
}
top_k_mappings["False_True_True_False_False"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 2,
    "search_patent_top_k": 8,
    "search_edu_top_k": 0,
    "search_esg_top_k": 0,
}
top_k_mappings["False_True_True_False_True"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 2,
    "search_patent_top_k": 4,
    "search_edu_top_k": 0,
    "search_esg_top_k": 4,
}
top_k_mappings["False_True_True_True_False"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 2,
    "search_patent_top_k": 4,
    "search_edu_top_k": 4,
    "search_esg_top_k": 0,
}
top_k_mappings["False_True_True_True_True"] = {
    "search_knowledge_base_top_k": 0,
    "search_report_top_k": 1,
    "search_patent_top_k": 4,
    "search_edu_top_k": 4,
    "search_esg_top_k": 4,
}
top_k_mappings["True_False_False_False_False"] = {
    "search_knowledge_base_top_k": 16,
    "search_report_top_k": 0,
    "search_patent_top_k": 0,
    "search_edu_top_k": 0,
    "search_esg_top_k": 0,
}
top_k_mappings["True_False_False_False_True"] = {
    "search_knowledge_base_top_k": 8,
    "search_report_top_k": 0,
    "search_patent_top_k": 0,
    "search_edu_top_k": 0,
    "search_esg_top_k": 8,
}
top_k_mappings["True_False_False_True_False"] = {
    "search_knowledge_base_top_k": 8,
    "search_report_top_k": 0,
    "search_patent_top_k": 0,
    "search_edu_top_k": 8,
    "search_esg_top_k": 0,
}
top_k_mappings["True_False_False_True_True"] = {
    "search_knowledge_base_top_k": 5,
    "search_report_top_k": 0,
    "search_patent_top_k": 0,
    "search_edu_top_k": 5,
    "search_esg_top_k": 6,
}
top_k_mappings["True_False_True_False_False"] = {
    "search_knowledge_base_top_k": 8,
    "search_report_top_k": 0,
    "search_patent_top_k": 8,
    "search_edu_top_k": 0,
    "search_esg_top_k": 0,
}
top_k_mappings["True_False_True_False_True"] = {
    "search_knowledge_base_top_k": 5,
    "search_report_top_k": 0,
    "search_patent_top_k": 5,
    "search_edu_top_k": 0,
    "search_esg_top_k": 6,
}
top_k_mappings["True_False_True_True_False"] = {
    "search_knowledge_base_top_k": 6,
    "search_report_top_k": 0,
    "search_patent_top_k": 5,
    "search_edu_top_k": 5,
    "search_esg_top_k": 0,
}
top_k_mappings["True_False_True_True_True"] = {
    "search_knowledge_base_top_k": 4,
    "search_report_top_k": 0,
    "search_patent_top_k": 4,
    "search_edu_top_k": 4,
    "search_esg_top_k": 4,
}
top_k_mappings["True_True_False_False_False"] = {
    "search_knowledge_base_top_k": 8,
    "search_report_top_k": 2,
    "search_patent_top_k": 0,
    "search_edu_top_k": 0,
    "search_esg_top_k": 0,
}
top_k_mappings["True_True_False_False_True"] = {
    "search_knowledge_base_top_k": 8,
    "search_report_top_k": 1,
    "search_patent_top_k": 0,
    "search_edu_top_k": 0,
    "search_esg_top_k": 4,
}
top_k_mappings["True_True_False_True_False"] = {
    "search_knowledge_base_top_k": 6,
    "search_report_top_k": 1,
    "search_patent_top_k": 0,
    "search_edu_top_k": 6,
    "search_esg_top_k": 0,
}
top_k_mappings["True_True_False_True_True"] = {
    "search_knowledge_base_top_k": 4,
    "search_report_top_k": 1,
    "search_patent_top_k": 0,
    "search_edu_top_k": 4,
    "search_esg_top_k": 4,
}
top_k_mappings["True_True_True_False_False"] = {
    "search_knowledge_base_top_k": 6,
    "search_report_top_k": 1,
    "search_patent_top_k": 6,
    "search_edu_top_k": 0,
    "search_esg_top_k": 0,
}
top_k_mappings["True_True_True_False_True"] = {
    "search_knowledge_base_top_k": 4,
    "search_report_top_k": 1,
    "search_patent_top_k": 4,
    "search_edu_top_k": 0,
    "search_esg_top_k": 4,
}
top_k_mappings["True_True_True_True_False"] = {
    "search_knowledge_base_top_k": 4,
    "search_report_top_k": 1,
    "search_patent_top_k": 4,
    "search_edu_top_k": 4,
    "search_esg_top_k": 0,
}
top_k_mappings["True_True_True_True_True"] = {
    "search_knowledge_base_top_k": 3,
    "search_report_top_k": 1,
    "search_patent_top_k": 3,
    "search_edu_top_k": 3,
    "search_esg_top_k": 3,
}
