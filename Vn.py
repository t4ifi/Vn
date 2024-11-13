import os

# Script Creado Por Andres Nuñez - t4ifi.
# No me hago responsable del uso indebido de esta herramienta.
class Colores:
    ROJO = "\033[31m"
    VERDE = "\033[32m"
    AZUL = "\033[34m"
    AMARILLO = "\033[33m"
    BLANCO = "\033[37m"
    RESET = "\033[39m"


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_query(query):
    clear_terminal()  
    print(f"{Colores.VERDE}[*] {query}{Colores.RESET}")
    input(f"\n{Colores.BLANCO}Presiona Enter para volver al menú...{Colores.RESET}")


def search_directory_listing(tld):
    query = f"site:{tld} intitle:index.of"
    print_query(query)

def search_exposed_configs(tld):
    query = f"site:{tld} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini"
    print_query(query)

def search_exposed_db_files(tld):
    query = f"site:{tld} ext:sql | ext:dbf | ext:mdb"
    print_query(query)

def search_exposed_log_files(tld):
    query = f"site:{tld} ext:log"
    print_query(query)

def search_backup_old_files(tld):
    query = f"site:{tld} ext:bak | ext:old | ext:backup"
    print_query(query)

def search_login_pages(tld):
    query = f"site:{tld} inurl:login"
    print_query(query)

def search_sql_errors(tld):
    query = f"site:{tld} inurl:error"
    print_query(query)

def search_public_docs(tld):
    query = f"site:{tld} ext:pdf | ext:doc | ext:txt | ext:xls"
    print_query(query)

def search_phpinfo(tld):
    query = f"site:{tld} inurl:phpinfo"
    print_query(query)

def search_wordpress(tld):
    query = f"site:{tld} inurl:wp-content | inurl:wp-admin"
    print_query(query)

def search_backdoors(tld):
    query = f"site:{tld} inurl:backdoor"
    print_query(query)

def search_install_setup_files(tld):
    query = f"site:{tld} inurl:install | inurl:setup"
    print_query(query)

def search_open_redirects(tld):
    query = f"site:{tld} inurl:redirect"
    print_query(query)

def search_apache_struts_rce(tld):
    query = f"site:{tld} inurl:struts"
    print_query(query)

def search_pastebin_entries(tld):
    query = f"site:pastebin.com {tld}"
    print_query(query)

def search_employees_linkedin(tld):
    query = f"site:linkedin.com {tld}"
    print_query(query)

def search_htaccess_sensitive_files(tld):
    query = f"site:{tld} inurl:/.htaccess"
    print_query(query)

def search_subdomains(tld):
    query = f"site:{tld} -www"
    print_query(query)

def search_sub_subdomains(tld):
    query = f"site:{tld} -www -ftp"
    print_query(query)

def search_in_github(tld):
    query = f"site:github.com {tld}"
    print_query(query)

def search_cross_domain(tld):
    query = f"site:{tld} inurl:crossdomain.xml"
    print_query(query)

def search_threatcrowd(tld):
    query = f"site:threatcrowd.org {tld}"
    print_query(query)

def search_swf(tld):
    query = f"site:{tld} ext:swf"
    print_query(query)

def search_mime_swf(tld):
    query = f"site:{tld} ext:swf | ext:mime"
    print_query(query)

def search_web_archive(tld):
    query = f"site:archive.org {tld}"
    print_query(query)

def search_certificate_transparency(tld):
    query = f"site:censys.io {tld} certificate"
    print_query(query)

def search_openbugbounty(tld):
    query = f"site:openbugbounty.org {tld}"
    print_query(query)

def search_in_reddit(tld):
    query = f"site:reddit.com {tld}"
    print_query(query)

def search_wp_config_backup(tld):
    query = f"site:{tld} inurl:wp-config.php"
    print_query(query)

def search_in_censys_ipv4(tld):
    query = f"site:censys.io {tld} ipv4"
    print_query(query)

def search_in_censys_domain(tld):
    query = f"site:censys.io {tld} domain"
    print_query(query)

def search_in_shodan(tld):
    query = f"site:shodan.io {tld}"
    print_query(query)

def search_vulnerable_servers(tld):
    query = f"site:shodan.io {tld} vulnerable"
    print_query(query)

def search_wp_content(tld):
    query = f"site:{tld} wp-content"
    print_query(query)

def search_juicy_info(tld):
    query = f"site:{tld} inurl:juicyinfo"
    print_query(query)

def search_main_yml(tld):
    query = f"site:{tld} inurl:main.yml"
    print_query(query)

def search_admin_portal(tld):
    query = f"site:{tld} inurl:admin"
    print_query(query)

def search_wordpress_juicy_file1(tld):
    query = f"site:{tld} inurl:wp-admin/juicyfile1"
    print_query(query)

def search_file_upload(tld):
    query = f"site:{tld} inurl:file-upload"
    print_query(query)

def search_wordpress_vulnerable_plugin(tld):
    query = f"site:{tld} inurl:wp-content/plugins"
    print_query(query)

def search_sensitive_file_sharing(tld):
    query = f"site:{tld} inurl:sharing"
    print_query(query)

def search_sensitive_admin_backup(tld):
    query = f"site:{tld} inurl:admin-backup"
    print_query(query)

def search_github_api(tld):
    query = f"site:github.com {tld} api"
    print_query(query)

def search_wordpress_juicy_file2(tld):
    query = f"site:{tld} inurl:wp-content/juicyfile2"
    print_query(query)

def search_drupal_login(tld):
    query = f"site:{tld} inurl:drupal/user/login"
    print_query(query)

def search_joomla_db_sql_file(tld):
    query = f"site:{tld} inurl:joomla/configuration.php"
    print_query(query)

def search_wordpress_juicy_file3(tld):
    query = f"site:{tld} inurl:wp-content/juicyfile3"
    print_query(query)

def search_rpc_protocol(tld):
    query = f"site:{tld} inurl:rpc"
    print_query(query)

def search_sensitive_jwks_rsa_file(tld):
    query = f"site:{tld} inurl:jwks-rsa"
    print_query(query)

def search_wordpress_backup_mysql_file(tld):
    query = f"site:{tld} inurl:wp-content/backup/mysql"
    print_query(query)

def search_sensitive_docker_compose(tld):
    query = f"site:{tld} inurl:docker-compose.yml"
    print_query(query)

def search_sensitive_file(tld):
    query = f"site:{tld} inurl:sensitivefile"
    print_query(query)

def search_sql_installs(tld):
    query = f"site:{tld} inurl:sql | inurl:install"
    print_query(query)


def show_menu():
    print(f"\n{Colores.AZUL}Menu de opciones:{Colores.RESET}")
    print("1.  Directory Listings")
    print("2.  Exposed Configuration files")
    print("3.  Exposed Database files")
    print("4.  Exposed log files")
    print("5.  Backup and old files")
    print("6.  Login pages")
    print("7.  SQL errors")
    print("8.  Publicly exposed documents")
    print("9.  phpinfo()")
    print("10. Find WordPress")
    print("11. Finding Backdoors")
    print("12. Install / Setup files")
    print("13. Open Redirects")
    print("14. Apache STRUTS RCE")
    print("15. Find Pastebin entries")
    print("16. Employees on LINKEDIN")
    print("17. .htaccess sensitive files")
    print("18. Find Subdomains")
    print("19. Find Sub-Subdomains")
    print("20. Find WordPress #2")
    print("21. Search in GITHUB")
    print("22. Test CrossDomain")
    print("23. Check in ThreatCrowd")
    print("24. Find SWF")
    print("25. Find MIME-SWF")
    print("26. Find SWF links in the past")
    print("27. Find MIME-SWF links in the past")
    print("28. Search in Web Archive #1")
    print("29. Search in Web Archive #2")
    print("30. Certificate Transparency")
    print("31. Search OpenBugBounty")
    print("32. Search in Reddit")
    print("33. Search WP Config Backup")
    print("34. Search in Censys (IPv4)")
    print("35. Search in Censys (Domain)")
    print("36. Search in Censys (Certificates)")
    print("37. Search in SHODAN")
    print("38. Vulnerable Servers")
    print("39. ArcGIS REST Services Directory")
    print("40. wp-content")
    print("41. Juicy Info")
    print("42. main.yml file")
    print("43. Admin Portal")
    print("44. Wordpress Juicy file 1")
    print("45. File Upload Vulnerable Wordpress Plugin")
    print("46. Sensitive File Sharing")
    print("47. Sensitive Admin Backup")
    print("48. Github API")
    print("49. Wordpress Juicy file 2")
    print("50. Drupal Login")
    print("51. Joomla Database/ Sql File")
    print("52. Wordpress Juicy file 3")
    print("53. Remote procedure call protocol")
    print("54. Sensitive File jwks-rsa file")
    print("55. Wordpress Backup Mysql file")
    print("56. Sensitive File Docker-Compose yml file")
    print("57. Sensitive File")
    print("58. Directories containing SQL Installs and/or SQL databases")
    print("59. Salir")

def main():
    clear_terminal()  
    print(f"{Colores.AZUL}Bienvenido al Buscador de Vulnerabilidades{Colores.RESET}\n")

    
    domain = input(f"{Colores.BLANCO}Introduce un dominio o TLD (Ej: .uy): {Colores.RESET}").strip()

    while True:
        show_menu()
        choice = input(f"\n{Colores.BLANCO}Selecciona una opción (1-59): {Colores.RESET}")

        if choice == "1":
            search_directory_listing(domain)
        elif choice == "2":
            search_exposed_configs(domain)
        elif choice == "3":
            search_exposed_db_files(domain)
        elif choice == "4":
            search_exposed_log_files(domain)
        elif choice == "5":
            search_backup_old_files(domain)
        elif choice == "6":
            search_login_pages(domain)
        elif choice == "7":
            search_sql_errors(domain)
        elif choice == "8":
            search_public_docs(domain)
        elif choice == "9":
            search_phpinfo(domain)
        elif choice == "10":
            search_wordpress(domain)
        elif choice == "11":
            search_backdoors(domain)
        elif choice == "12":
            search_install_setup_files(domain)
        elif choice == "13":
            search_open_redirects(domain)
        elif choice == "14":
            search_apache_struts_rce(domain)
        elif choice == "15":
            search_pastebin_entries(domain)
        elif choice == "16":
            search_employees_linkedin(domain)
        elif choice == "17":
            search_htaccess_sensitive_files(domain)
        elif choice == "18":
            search_subdomains(domain)
        elif choice == "19":
            search_sub_subdomains(domain)
        elif choice == "20":
            search_wordpress(domain) 
        elif choice == "21":
            search_in_github(domain)
        elif choice == "22":
            search_cross_domain(domain)
        elif choice == "23":
            search_threatcrowd(domain)
        elif choice == "24":
            search_swf(domain)
        elif choice == "25":
            search_mime_swf(domain)
        elif choice == "26":
            search_swf(domain)
        elif choice == "27":
            search_mime_swf(domain)
        elif choice == "28":
            search_web_archive(domain)
        elif choice == "29":
            search_web_archive(domain)
        elif choice == "30":
            search_certificate_transparency(domain)
        elif choice == "31":
            search_openbugbounty(domain)
        elif choice == "32":
            search_in_reddit(domain)
        elif choice == "33":
            search_wp_config_backup(domain)
        elif choice == "34":
            search_in_censys_ipv4(domain)
        elif choice == "35":
            search_in_censys_domain(domain)
        elif choice == "36":
            search_in_censys_ipv4(domain)
        elif choice == "37":
            search_in_shodan(domain)
        elif choice == "38":
            search_vulnerable_servers(domain)
        elif choice == "39":
            search_wp_content(domain)
        elif choice == "40":
            search_juicy_info(domain)
        elif choice == "41":
            search_main_yml(domain)
        elif choice == "42":
            search_admin_portal(domain)
        elif choice == "43":
            search_wordpress_juicy_file1(domain)
        elif choice == "44":
            search_file_upload(domain)
        elif choice == "45":
            search_wordpress_vulnerable_plugin(domain)
        elif choice == "46":
            search_sensitive_file_sharing(domain)
        elif choice == "47":
            search_sensitive_admin_backup(domain)
        elif choice == "48":
            search_github_api(domain)
        elif choice == "49":
            search_wordpress_juicy_file2(domain)
        elif choice == "50":
            search_drupal_login(domain)
        elif choice == "51":
            search_joomla_db_sql_file(domain)
        elif choice == "52":
            search_wordpress_juicy_file3(domain)
        elif choice == "53":
            search_rpc_protocol(domain)
        elif choice == "54":
            search_sensitive_jwks_rsa_file(domain)
        elif choice == "55":
            search_wordpress_backup_mysql_file(domain)
        elif choice == "56":
            search_sensitive_docker_compose(domain)
        elif choice == "57":
            search_sensitive_file(domain)
        elif choice == "58":
            search_sql_installs(domain)
        elif choice == "59":
            clear_terminal()  
            print(f"{Colores.ROJO}Saliendo...\n{Colores.RESET}")
            break
        else:
            clear_terminal()  
            print(f"{Colores.ROJO}Opción inválida. Intenta nuevamente.{Colores.RESET}\n")

if __name__ == "__main__":
    main()

