# I wrote this originaly to run in the background, not stopping until a product was available, which would then let me know through the pushbullet API.  I modified it to only run once, and to record the times from both
# syncronous and multiprocessing.

from selenium import webdriver
from pushbullet import PushBullet #need to install this with pip
from selenium.webdriver.chrome.options import Options
from msedge.selenium_tools import Edge, EdgeOptions
import multiprocessing
import random
import time

newegg = "https://www.newegg.com/p/pl?N=100007709%20601357282&PageSize=96"
bestbuy = "https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203080"
pb = PushBullet('(Pushbullet encryption key)')

opts = EdgeOptions()
opts.use_chromium = True
#opts.add_argument("headless")
opts.add_argument("disable-gpu")

#find the name of the element, and check to see the status of the item
def ParseContent(searchProductsText, count, site):
    compare = ['Sold Out', 'SOLD OUT', 'OUT OF STOCK', 'Out of Stock', 'Coming Soon', 'COMING SOON']
    searchName = ['3070', '3080']

    #used to verify both versions have the same total elements
    verifyCount = 0

    #takes each list element and splits it by a return, finds the item name and checks to see if a 'searchName' element is included.
    #finally, it checks to see if the element from the original list includes one of the keywords from the 'compare' list.
    for product in searchProductsText:
        inStock = False
        findName = product.split('\n')
        name = ''
        for found in findName:
            for x in searchName:
                if x in found:
                    name = found
                    verifyCount += 1
                    for state in compare:
                        if state in product:
                            inStock = False
                            break
                        else:
                            inStock = True
                        
                    if inStock == False:
                        print(site + ' - ' + str(verifyCount) + ' - ' + name + ' - still out of stock, retrying')
                    else:
                        print('found')
                        print(name + ' in stock!')
                        #pb.push_note(name, "Go get it dude!")
                        return True
    return True

def StartWebSearch(website, xPath, name, site):
    driver = Edge(options=opts)
    executor_url = driver.command_executor._url

    complete = False
    count = 0
    errorCount = 1
    
    driver.get(website)

    while complete == False:
        try:
            count += 1
            #randomNum = random.uniform(.5, 4)

            driver.implicitly_wait(15)

            searchTable = driver.find_element_by_xpath(xPath)
            searchProducts = searchTable.find_elements_by_class_name(name)
            searchProductsText = []
            
            #putting the text of the web elements into a seperate list reduces the amount of requests being made to the website when parsing.
            for sText in searchProducts:
                searchProductsText.append(sText.text)

            complete = ParseContent(searchProductsText, count, site)
            
            print('\n')
            #time.sleep(randomNum)
            #driver.refresh()

        #More useful for original script which had this running continuously.
        except Exception as e:
            if errorCount % 10 == 0:
                #pb.push_note("Check Program!", "Something is wrong.")
                print(e)
                continue
            else:
                driver.close()
                #I was finding that a simple page refresh wasn't correcting some http errors that were occuring, so this piece of code is required to restart the driver after the close call.
                driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={}, options=opts)
                driver.get(website)
                continue
            errorCount += 1

    driver.quit()

if __name__ == '__main__':
    bestbuyXPath = "//*[@id='main-results']/ol"
    neweggXPath = "//*[@id='app']/div[2]/section/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]"
    bestbuyName = "sku-item"
    neweggName = "item-cell"

    print('starting syncronous run:\n')
    syncStartTime = time.time()

    StartWebSearch(bestbuy, bestbuyXPath, bestbuyName, 'BestBuy')
    StartWebSearch(newegg, neweggXPath, neweggName, 'newegg')

    syncEndTime = time.time() - syncStartTime

    multiStartTime = time.time()

    print('starting multiprocessing run:\n')
    p1 = multiprocessing.Process(target=StartWebSearch, args=(bestbuy, bestbuyXPath, bestbuyName, 'BestBuy'))
    p2 = multiprocessing.Process(target=StartWebSearch, args=(newegg, neweggXPath, neweggName, 'Newegg'))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    multiEndTime = time.time() - multiStartTime

    print('Sync complete time: ' + str(syncEndTime))
    print('Multiprocessing complete time: ' + str(multiEndTime))
    
