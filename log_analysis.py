#!/usr/bin/env python

import psycopg2


error = """ SELECT round((errorentries*100.0)/(errorentries+rightentries),3)
            as errorpercent, errordate
            FROM errors_entries, right_entries
            WHERE errors_entries.errordate = right_entries.rightdate
            AND round((errorentries*100.0)/(errorentries+rightentries),3)>1
            ORDER BY errorpercent DESC """


TopThreeArticles = """SELECT title, count(*) AS views
                      FROM articles,log
                      WHERE articles.slug= substring(log.path,10)
                      AND log.status = '200 OK'
                      GROUP BY articles.title
                      ORDER BY views DESC
                      LIMIT 3; """


TopAuthors = """SELECT authors.name , count(*) AS num
                FROM articles, authors , log
                WHERE log.status LIKE '%200%'
                AND authors.id = articles.author
                AND articles.slug = substring(log.path,10)
                GROUP BY authors.name
                ORDER BY num DESC;"""

database_name = "news"
question3 = "What are the most popular three articles of all time?"
question2 = "Who are the most popular article authors of all time?"
question1 = "On which days did more than 1 percent of requests lead to error?"


def query_answers(query):
    db = psycopg2.connect(database=database_name)
    cursor = db.cursor()
    cursor.execute(query)
    answers = cursor.fetchall()
    return answers


def errors(query1):
    answer1 = query_answers(query1)
    print(question1)
    for ar in answer1:
        print("date: " + str(ar[1]) + " - precentage of errors: " +
              str(ar[0]) + "% \n")
    print('*************************************************')


def top_authors(query2):
    answer2 = query_answers(query2)
    print(question2)
    for ar in answer2:
        print(str(ar[0]) + " - " + str(ar[1]) + " views.\n")
    print('*************************************************')


def top_three_articles(query3):
    answer3 = query_answers(query3)
    print(question3)
    for ar in answer3:
        print(str(ar[0]) + " - " + str(ar[1]) + " views.\n")
    print('*************************************************')


errors(error)
top_authors(TopAuthors)
top_three_articles(TopThreeArticles)
