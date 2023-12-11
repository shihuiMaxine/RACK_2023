import rack
from rack import main
import ast
import sys
import extractor
import extractor.GitHubClient
import requests
from bs4 import BeautifulSoup
import re
import csv
# print (sys.argv)
totalcont=[]
lista=[]
# dicta=[]
dicta={}
# print (sys.argv[2:])
# stringquery=' '.join(sys.argv[2:])
# print(stringquery)

# print("hello")
# query = "send email"
stringquery="Accessing a list of rows from mySQL table"
question="https://api.github.com/search/code?q="
listquery=stringquery.split(" ")
for i in range (0, len(listquery)):
    # if i != (len(stringquery)-1):
    question+=listquery[i] + "+"
    # else:
        # question+=i
question += "in:file+language:python"

call_url ="https://api.github.com/search/code?q=Accessing+a+list+of+rows+from+mySQL+table+in:file+language:python"
# print(call_url)
# print(question)
result = extractor.GitHubClient.execute_github_call(call_url)
htmlresult=result.split(",")
listgit=[]
for i in htmlresult:
    if "html_url" in i:
        if ".py" in i:
            # print("html_url:")
            # print(i[12:len(i)-1])
            listgit.append(i[12:len(i)-1])
            
# extractor.GitHubClient.execute_github_call(call_url)
            # extractor.getcodeapi.github_url_to_raw_url(i[12:len(i)-1])
apitoken=main.main(stringquery)
print(apitoken)
k=["execute", "len", "cursor", "append", "range"]

def github_url_to_raw_url(github_url):
    # Parse the GitHub URL
    parts = github_url.split("/")
    
    # Extract the repository owner, repository name, and branch or commit hash
    owner, repo, branch_or_commit = parts[3], parts[4], parts[6]
    
    # Extract the path to the file
    file_path = "/".join(parts[7:])
    response = requests.get(github_url)
    response.raise_for_status() 
    raw_url=""
    if response.status_code == 200:

    
        # Construct the raw URL
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch_or_commit}/{file_path}"
        response = requests.get(raw_url)
        response.raise_for_status() 
        # print(raw_url)
        if response.status_code == 200:

            return github_url,raw_url
        else:
            return "",""
# for i in listgit:
#     github_url,raw_url = github_url_to_raw_url(i)
#     print(github_url)
#     print(raw_url)

giturllist=[]
totalraw=[]
n=0
for i in listgit:
    # if n==0:
    github_url = i

    # Convert to raw URL
    giturl,raw_url = github_url_to_raw_url(github_url)
    if giturl != "":
        totalraw.append(raw_url)
        giturllist.append(giturl)

        # Print the raw URL
        print(raw_url)
    # n+=1
k=["execute", "len", "cursor", "append", "range"]
codelist=[]
for q in range(0,len(totalraw)):
    j=totalraw[q]
    githuburl = giturllist[q]
    codecontent=[]
    apicontent=[]
    response = requests.get(j)
    
    code_content = response.text
    # Your input code
    input_code = code_content
    # if q == 0:
    #     # print(input_code)
    codelist.append(input_code)

# k=apitoken
# def remove_comments(input_code):
#     # Use a regular expression to match and remove comments
#     cleaned_code = re.sub(r'^\s*#.*|(""")[\s\S]*?\1|(\'\'\')[\s\S]*?\2', '', input_code)
#     return cleaned_code

# import inspect

# def find_definition(input_code, m1):
#     try:
#         # Get the source code of the object with the given name
#         source_code = input_code
#         print(f"Definition of {name}:\n{source_code}\n{'='*50}\n")
#     except (NameError, TypeError, IOError, AttributeError):
#         print(f"Could not find definition for {name}\n{'='*50}\n")

# # List of names to search for
# names_to_search = ["execute", "len", "cursor", "append", "range"]

# # Find definitions for each name



# def find_code_snippet(code_text, target_content):
#     # print(code_text)
#     # code_without_comments = remove_comments_from_code(code_text)
#     # Parse the code
#     # print(code_without_comments)
#     cleaned_code = remove_comments(code_text)
#     # print(cleaned_code)
#     # try:
#     parsed_code = ast.parse(str(cleaned_code))
#     # except:
#     #     ast.parse(str(" "))
#     # print()

#     # Define a visitor class to traverse the AST
#     class FindContentVisitor(ast.NodeVisitor):
#         def __init__(self, target_content):
#             self.target_content = target_content
#             self.found_code = []

#         def visit_FunctionDef(self, node):
#             # Check if the function contains the target content
#             function_code = ast.get_source_segment(code_text, node)
#             if self.target_content in function_code:
#                 self.found_code.append(function_code)

#     # Create an instance of the visitor
#     visitor = FindContentVisitor(target_content)

#     # Visit the AST
#     visitor.visit(parsed_code)

#     return visitor.found_code

# for q in range(0,len(totalraw)):
#     j=totalraw[q]
#     githuburl = giturllist[q]
#     codecontent=[]
#     apicontent=[]
#     response = requests.get(j)
    
#     code_content = response.text
#     # Your input code
#     input_code = code_content
#     for name in names_to_search:
#     # find_definition(name)
#         find_definition(input_code, name)

#     # Target content to find
#     target_content = 'SMTP'
#     # k=['MIMEText', 'sendmail','SMTP','MIMEMultipart','login']
#     # k=['hexdigest', 'md5', 'encode', 'update', 'hashlib']
#     # k=["range", "gcd", "len", "int", "set"]
    

#     # k=['MIMEMultipart']
#     # Find the code snippets containing the target content
#     for m in k:
#         m1=(" "+m+"(") or("."+m+"(")
#         m1=m+"("
#         try:
#             output_code_snippets =find_code_snippet(input_code, m1)

#         except:
#             break
#         for i, snippet in enumerate(output_code_snippets, 1):
#             # print(f"Output {m}:\n{snippet}\n{'='*40}")
#             if m not in apicontent:
#                 apicontent.append(m)
#             # print(apicontent)
#             codecontent.append(f"Output {m}:\n{snippet}\n{'='*40}")
#     # print("hello")
#     # print(codecontent[0])
#     # print("hello")
#     if len(apicontent)!=0:
#         datacontent1=[githuburl,j,apicontent,codecontent]
#         totalcont.append(datacontent1)
        

#         # writer.writerow(datacontent1)



# for i in range (0, len(k)):
#     for x in totalcont:
#         # print(x[0])
#         if (len(k)-i ) == len(x[2]):
#             # print(len(k)-i)
#             # print(x[2])
#             # print(x[0])
#             response = requests.get(x[1])
#             code = response.text
#             pattern = r"\w+\("
#             method_names = re.findall(pattern, code)
#             list1=[]
#             string1=""
#             for name in method_names:
#                 nameele=name[0:len(name)-1]
#                 if nameele not in list1:
#                     if nameele != "print":
#                         list1.append(nameele)
#                         string1+=nameele
#                         string1+=" "
#             totalnum=len(list1)+i
#             perc=(len(x[2]))/(len(list1)+i)
#             # print(list1)
#             # print(perc)
#             lista.append(perc)
#             dicta[perc]=x



            
#             # x.append(perc)


#             # writer.writerow(x)
#                 # writer.writerow(x)
# co =0
# # print(lista.sort())
# lista.sort(reverse=True)
# # print(dicta[0])
# # print(lista)
# for i in lista:
#     listr=[]
#     if co ==1:
#         # print(dicta[i])
#         listr=dicta[i]
#         # for j in dicta[i]:
#         #     listr.append(j)
#         listr.append(i)
#         # print(len(listr[3]))
#         for z in listr[3]:
#             u=0
#             # print(z)
#     if i > 4:
#         break


#     co +=1
        

# import re

def find_definition_with_content(code, names):
    definitions = {}
    
    for name in names:
        pattern = re.compile(f'def {name}\(.*?\):(.+?)(?=(\ndef |\Z))', re.DOTALL)
        match = pattern.search(code)
        if match:
            definitions[name] = match.group(0).strip()

    return definitions

# Example usage:
code_snippet = """
from django.db import ProgrammingError
from django.utils.functional import cached_property


class BaseDatabaseFeatures:
    # An optional tuple indicating the minimum supported database version.
    minimum_database_version = None
    gis_enabled = False
    # Oracle can't group by LOB (large object) data types.
    allows_group_by_lob = True
    allows_group_by_selected_pks = False
    allows_group_by_select_index = True
    empty_fetchmany_value = []
    update_can_self_select = True
    # Does the backend support self-reference subqueries in the DELETE
    # statement?
    delete_can_self_reference_subquery = True

    # Does the backend distinguish between '' and None?
    interprets_empty_strings_as_nulls = False

    # Does the backend allow inserting duplicate NULL rows in a nullable
    # unique field? All core backends implement this correctly, but other
    # databases such as SQL Server do not.
    supports_nullable_unique_constraints = True

    # Does the backend allow inserting duplicate rows when a unique_together
    # constraint exists and some fields are nullable but not all of them?
    supports_partially_nullable_unique_constraints = True

    # Does the backend supports specifying whether NULL values should be
    # considered distinct in unique constraints?
    supports_nulls_distinct_unique_constraints = False

    # Does the backend support initially deferrable unique constraints?
    supports_deferrable_unique_constraints = False

    can_use_chunked_reads = True
    can_return_columns_from_insert = False
    can_return_rows_from_bulk_insert = False
    has_bulk_insert = True
    uses_savepoints = True
    can_release_savepoints = False

    # If True, don't use integer foreign keys referring to, e.g., positive
    # integer primary keys.
    related_fields_match_type = False
    allow_sliced_subqueries_with_in = True
    has_select_for_update = False
    has_select_for_update_nowait = False
    has_select_for_update_skip_locked = False
    has_select_for_update_of = False
    has_select_for_no_key_update = False
    # Does the database's SELECT FOR UPDATE OF syntax require a column rather
    # than a table?
    select_for_update_of_column = False

    # Does the default test database allow multiple connections?
    # Usually an indication that the test database is in-memory
    test_db_allows_multiple_connections = True

    # Can an object be saved without an explicit primary key?
    supports_unspecified_pk = False

    # Can a fixture contain forward references? i.e., are
    # FK constraints checked at the end of transaction, or
    # at the end of each save operation?
    supports_forward_references = True

    # Does the backend truncate names properly when they are too long?
    truncates_names = False

    # Is there a REAL datatype in addition to floats/doubles?
    has_real_datatype = False
    supports_subqueries_in_group_by = True

    # Does the backend ignore unnecessary ORDER BY clauses in subqueries?
    ignores_unnecessary_order_by_in_subqueries = True

    # Is there a true datatype for uuid?
    has_native_uuid_field = False

    # Is there a true datatype for timedeltas?
    has_native_duration_field = False

    # Does the database driver supports same type temporal data subtraction
    # by returning the type used to store duration field?
    supports_temporal_subtraction = False

    # Does the __regex lookup support backreferencing and grouping?
    supports_regex_backreferencing = True

    # Can date/datetime lookups be performed using a string?
    supports_date_lookup_using_string = True

    # Can datetimes with timezones be used?
    supports_timezones = True

    # Does the database have a copy of the zoneinfo database?
    has_zoneinfo_database = True

    # When performing a GROUP BY, is an ORDER BY NULL required
    # to remove any ordering?
    requires_explicit_null_ordering_when_grouping = False

    # Does the backend order NULL values as largest or smallest?
    nulls_order_largest = False

    # Does the backend support NULLS FIRST and NULLS LAST in ORDER BY?
    supports_order_by_nulls_modifier = True

    # Does the backend orders NULLS FIRST by default?
    order_by_nulls_first = False

    # The database's limit on the number of query parameters.
    max_query_params = None

    # Can an object have an autoincrement primary key of 0?
    allows_auto_pk_0 = True

    # Do we need to NULL a ForeignKey out, or can the constraint check be
    # deferred
    can_defer_constraint_checks = False

    # Does the backend support tablespaces? Default to False because it isn't
    # in the SQL standard.
    supports_tablespaces = False

    # Does the backend reset sequences between tests?
    supports_sequence_reset = True

    # Can the backend introspect the default value of a column?
    can_introspect_default = True

    # Confirm support for introspected foreign keys
    # Every database can do this reliably, except MySQL,
    # which can't do it for MyISAM tables
    can_introspect_foreign_keys = True

    # Map fields which some backends may not be able to differentiate to the
    # field it's introspected as.
    introspected_field_types = {
        "AutoField": "AutoField",
        "BigAutoField": "BigAutoField",
        "BigIntegerField": "BigIntegerField",
        "BinaryField": "BinaryField",
        "BooleanField": "BooleanField",
        "CharField": "CharField",
        "DurationField": "DurationField",
        "GenericIPAddressField": "GenericIPAddressField",
        "IntegerField": "IntegerField",
        "PositiveBigIntegerField": "PositiveBigIntegerField",
        "PositiveIntegerField": "PositiveIntegerField",
        "PositiveSmallIntegerField": "PositiveSmallIntegerField",
        "SmallAutoField": "SmallAutoField",
        "SmallIntegerField": "SmallIntegerField",
        "TimeField": "TimeField",
    }

    # Can the backend introspect the column order (ASC/DESC) for indexes?
    supports_index_column_ordering = True

    # Does the backend support introspection of materialized views?
    can_introspect_materialized_views = False

    # Support for the DISTINCT ON clause
    can_distinct_on_fields = False

    # Does the backend prevent running SQL queries in broken transactions?
    atomic_transactions = True

    # Can we roll back DDL in a transaction?
    can_rollback_ddl = False

    schema_editor_uses_clientside_param_binding = False

    # Can we issue more than one ALTER COLUMN clause in an ALTER TABLE?
    supports_combined_alters = False

    # Does it support foreign keys?
    supports_foreign_keys = True

    # Can it create foreign key constraints inline when adding columns?
    can_create_inline_fk = True

    # Can an index be renamed?
    can_rename_index = False

    # Does it automatically index foreign keys?
    indexes_foreign_keys = True

    # Does it support CHECK constraints?
    supports_column_check_constraints = True
    supports_table_check_constraints = True
    # Does the backend support introspection of CHECK constraints?
    can_introspect_check_constraints = True

    # Does the backend support 'pyformat' style ("... %(name)s ...", {'name': value})
    # parameter passing? Note this can be provided by the backend even if not
    # supported by the Python driver
    supports_paramstyle_pyformat = True

    # Does the backend require literal defaults, rather than parameterized ones?
    requires_literal_defaults = False

    # Does the backend support functions in defaults?
    supports_expression_defaults = True

    # Does the backend support the DEFAULT keyword in insert queries?
    supports_default_keyword_in_insert = True

    # Does the backend support the DEFAULT keyword in bulk insert queries?
    supports_default_keyword_in_bulk_insert = True

    # Does the backend require a connection reset after each material schema change?
    connection_persists_old_columns = False

    # What kind of error does the backend throw when accessing closed cursor?
    closed_cursor_error_class = ProgrammingError

    # Does 'a' LIKE 'A' match?
    has_case_insensitive_like = False

    # Suffix for backends that don't support "SELECT xxx;" queries.
    bare_select_suffix = ""

    # If NULL is implied on columns without needing to be explicitly specified
    implied_column_null = False

    # Does the backend support "select for update" queries with limit (and offset)?
    supports_select_for_update_with_limit = True

    # Does the backend ignore null expressions in GREATEST and LEAST queries unless
    # every expression is null?
    greatest_least_ignores_nulls = False

    # Can the backend clone databases for parallel test execution?
    # Defaults to False to allow third-party backends to opt-in.
    can_clone_databases = False

    # Does the backend consider table names with different casing to
    # be equal?
    ignores_table_name_case = False

    # Place FOR UPDATE right after FROM clause. Used on MSSQL.
    for_update_after_from = False

    # Combinatorial flags
    supports_select_union = True
    supports_select_intersection = True
    supports_select_difference = True
    supports_slicing_ordering_in_compound = False
    supports_parentheses_in_compound = True
    requires_compound_order_by_subquery = False

    # Does the database support SQL 2003 FILTER (WHERE ...) in aggregate
    # expressions?
    supports_aggregate_filter_clause = False

    # Does the backend support indexing a TextField?
    supports_index_on_text_field = True

    # Does the backend support window expressions (expression OVER (...))?
    supports_over_clause = False
    supports_frame_range_fixed_distance = False
    supports_frame_exclusion = False
    only_supports_unbounded_with_preceding_and_following = False

    # Does the backend support CAST with precision?
    supports_cast_with_precision = True

    # How many second decimals does the database return when casting a value to
    # a type with time?
    time_cast_precision = 6

    # SQL to create a procedure for use by the Django test suite. The
    # functionality of the procedure isn't important.
    create_test_procedure_without_params_sql = None
    create_test_procedure_with_int_param_sql = None

    # SQL to create a table with a composite primary key for use by the Django
    # test suite.
    create_test_table_with_composite_primary_key = None

    # Does the backend support keyword parameters for cursor.callproc()?
    supports_callproc_kwargs = False

    # What formats does the backend EXPLAIN syntax support?
    supported_explain_formats = set()

    # Does the backend support the default parameter in lead() and lag()?
    supports_default_in_lead_lag = True

    # Does the backend support ignoring constraint or uniqueness errors during
    # INSERT?
    supports_ignore_conflicts = True
    # Does the backend support updating rows on constraint or uniqueness errors
    # during INSERT?
    supports_update_conflicts = False
    supports_update_conflicts_with_target = False

    # Does this backend require casting the results of CASE expressions used
    # in UPDATE statements to ensure the expression has the correct type?
    requires_casted_case_in_updates = False

    # Does the backend support partial indexes (CREATE INDEX ... WHERE ...)?
    supports_partial_indexes = True
    supports_functions_in_partial_indexes = True
    # Does the backend support covering indexes (CREATE INDEX ... INCLUDE ...)?
    supports_covering_indexes = False
    # Does the backend support indexes on expressions?
    supports_expression_indexes = True
    # Does the backend treat COLLATE as an indexed expression?
    collate_as_index_expression = False

    # Does the database allow more than one constraint or index on the same
    # field(s)?
    allows_multiple_constraints_on_same_fields = True

    # Does the backend support boolean expressions in SELECT and GROUP BY
    # clauses?
    supports_boolean_expr_in_select_clause = True
    # Does the backend support comparing boolean expressions in WHERE clauses?
    # Eg: WHERE (price > 0) IS NOT NULL
    supports_comparing_boolean_expr = True

    # Does the backend support JSONField?
    supports_json_field = True
    # Can the backend introspect a JSONField?
    can_introspect_json_field = True
    # Does the backend support primitives in JSONField?
    supports_primitives_in_json_field = True
    # Is there a true datatype for JSON?
    has_native_json_field = False
    # Does the backend use PostgreSQL-style JSON operators like '->'?
    has_json_operators = False
    # Does the backend support __contains and __contained_by lookups for
    # a JSONField?
    supports_json_field_contains = True
    # Does value__d__contains={'f': 'g'} (without a list around the dict) match
    # {'d': [{'f': 'g'}]}?
    json_key_contains_list_matching_requires_list = False
    # Does the backend support JSONObject() database function?
    has_json_object_function = True

    # Does the backend support column collations?
    supports_collation_on_charfield = True
    supports_collation_on_textfield = True
    # Does the backend support non-deterministic collations?
    supports_non_deterministic_collations = True

    # Does the backend support column and table comments?
    supports_comments = False
    # Does the backend support column comments in ADD COLUMN statements?
    supports_comments_inline = False

    # Does the backend support stored generated columns?
    supports_stored_generated_columns = False
    # Does the backend support virtual generated columns?
    supports_virtual_generated_columns = False

    # Does the backend support the logical XOR operator?
    supports_logical_xor = False

    # Set to (exception, message) if null characters in text are disallowed.
    prohibits_null_characters_in_text_exception = None

    # Does the backend support unlimited character columns?
    supports_unlimited_charfield = False

    # Collation names for use by the Django test suite.
    test_collations = {
        "ci": None,  # Case-insensitive.
        "cs": None,  # Case-sensitive.
        "non_default": None,  # Non-default.
        "swedish_ci": None,  # Swedish case-insensitive.
        "virtual": None,  # A collation that can be used for virtual columns.
    }
    # SQL template override for tests.aggregation.tests.NowUTC
    test_now_utc_template = None

    # SQL to create a model instance using the database defaults.
    insert_test_table_with_defaults = None

    # A set of dotted paths to tests in Django's test suite that are expected
    # to fail on this database.
    django_test_expected_failures = set()
    # A map of reasons to sets of dotted paths to tests in Django's test suite
    # that should be skipped for this database.
    django_test_skips = {}

    def __init__(self, connection):
        self.connection = connection

    @cached_property
    def supports_explaining_query_execution(self):

        return self.connection.ops.explain_prefix is not None

    @cached_property
    def supports_transactions(self):

        with self.connection.cursor() as cursor:
            cursor.execute("CREATE TABLE ROLLBACK_TEST (X INT)")
            self.connection.set_autocommit(False)
            cursor.execute("INSERT INTO ROLLBACK_TEST (X) VALUES (8)")
            self.connection.rollback()
            self.connection.set_autocommit(True)
            cursor.execute("SELECT COUNT(X) FROM ROLLBACK_TEST")
            (count,) = cursor.fetchone()
            cursor.execute("DROP TABLE ROLLBACK_TEST")
        return count == 0

    def allows_group_by_selected_pks_on_model(self, model):
        if not self.allows_group_by_selected_pks:
            return False
        return model._meta.managed

"""

function_names_to_find = ["execute", "len", "cursor", "append", "range","supports_transactions"]
found_definitions = find_definition_with_content(code_snippet, function_names_to_find)
# for x in codelist:
#     found_definitions = find_definition_with_content(x, function_names_to_find)
    # found_definitions = find_definition_with_content(codelist[2], function_names_to_find)
for name, definition in found_definitions.items():
    print("found definition")
    print(f"Found definition for '{name}':\n{definition}")
# print(codelist[0])
