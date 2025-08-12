from schemas.QAmodel import QAItem
from typing import List
#TODO:get question mechanism which gets the question based on interview_id and question_id
def get_current_question_item(interview_id, question_id):
    questions: List[QAItem] = [
        QAItem(
            question="Introduce yourself with a focus on your technical background and skills relevant to software engineering.",
            answer=(
                "Points an ideal answer could include: educational background, programming languages known, major academic projects, "
                "technical certifications, internships, relevant tools/technologies used, and any notable achievements in the field."
            )
        ),
        QAItem(
            question="What is polymorphism in Object-Oriented Programming? Provide an example.",
            answer=(
                "Points an ideal answer could include: definition of polymorphism, difference between compile-time and runtime polymorphism, "
                "examples in Java/Python/C++, method overloading, method overriding, benefits of polymorphism in code flexibility and reusability."
            )
        ),
        QAItem(
            question="Explain the differences between processes and threads.",
            answer=(
                "Points an ideal answer could include: definition of process and thread, memory allocation differences, context switching, "
                "communication overhead, shared memory in threads vs isolated memory in processes, examples of use cases, "
                "impact on performance and concurrency."
            )
        ),
        QAItem(
            question="Describe how a TCP three-way handshake works.",
            answer=(
                "Points an ideal answer could include: steps of SYN, SYN-ACK, ACK; purpose of each step; establishment of a reliable connection; "
                "role in connection setup; port numbers; sequence numbers; example packet flow."
            )
        ),
        QAItem(
            question="What is database normalization? Mention some normal forms.",
            answer=(
                "Points an ideal answer could include: definition of normalization, goals like reducing redundancy and improving integrity, "
                "1NF, 2NF, 3NF explanations, functional dependencies, examples of converting unnormalized data to normalized form."
            )
        ),
        QAItem(
            question="Explain the difference between an abstract class and an interface.",
            answer=(
                "Points an ideal answer could include: definition of abstract class, definition of interface, method implementation rules, "
                "support for multiple inheritance via interfaces, default/static methods in interfaces (Java 8+), use cases for each."
            )
        ),
        QAItem(
            question="How does a hash table work, and what are some common collision resolution techniques?",
            answer=(
                "Points an ideal answer could include: key-value storage mechanism, hash function role, load factor, "
                "collision resolution methods (chaining, open addressing, linear probing, quadratic probing, double hashing), "
                "time complexity analysis for average and worst case."
            )
        )
    ]
    return questions[question_id]
 