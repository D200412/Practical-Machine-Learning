# Practical Machine Learning

## 1.1 Course Introduction

### Industrial ML Applications(工业机器学习应用)

**Manufacturing(制造业):**Predictive maintenance(预测性维护), quality control(质量控制)
**Retail(销售业):**Recommendation(推荐系统), chatbot(聊天机器人), demand forecasting(需求预测)
**Healthcare(医疗):**Alerts from real-time patient data(基于实时患者数据的预警), disease identification(疾病识别)
**Finace(金融):**Fraud detection(欺诈检测), application processing(申请处理)
**Automobile(汽车):**Breakdown prediction(故障预测), self-driving(自动驾驶)

### ML Workflow

![image-20260707235141045](http://look-this-world.oss-cn-qingdao.aliyuncs.com/HelloWorld/image-20260707235141045.png)

### Challenges

- **Formulate(制定) problem:** focus on the most impactful(有影响力的) industrial problems (self-service supermarket,self-driving cars)
- **Data:** high-quality data is scarce(稀缺), privacy issues(问题)
- **Train models:** models are more and more complex, data-hungry, expensive
- **Deploy(部署) models:** heavy computation is not suitable for real-time inference(推理)
- **Monitor(监控):** data distributions(分布) shifts(转变), fairness issues

### Roles

**Domain(领域) experts:** have business insights(洞察力), know what data is important and where to find it, identify(识别) the real impact of a ML model
**Data scientists:** full stack on data mining(挖掘), model training and deployment(部署)
**ML experts:** customize(定制) SOTA ML models
**SDE(软件开发工程师):** develop/maintain(维护) data pipelines(管道), model training and serving pipelines



## 1.2 Data Acquisition(采集)

Focusing primarily on **Discover or integrate(整合) data**；**Generate(生成) Data**.

### Discover what data is available(可用)

- Identify(识别) existing(现有的) datasets
- Find benchmark(基准) datasets to evaluate(评估) a new idea 
  - E.g. A diverse(多样的) set of small to medium(中等的) datasets for a new hyper-parameter tuning(调优) algorithm
  - E.g. Large scale(大规模) datasets for a very big deep neural network(神经网络)
- Collect new data
  - E.g. driving videos covering different driving scenarios(场景)

### Popular ML datasets

at https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research

### Where to Find Datasets

- [Paperswithcodes Datasets](https://huggingface.co/papers/trending):academic datasets with leaderboard
- [Kaggle Datasets](https://www.kaggle.com/datasets): ML datasets uploaded(上传) by data scientists
- [Google Dataset search](https://datasetsearch.research.google.com/): search datasets in the Web
- Various toolkits datasets: [tensorflow](https://www.tensorflow.org/datasets?hl=zh-cn), [huggingface](https://huggingface.co/docs/datasets/index)
- Various conference(会议)/company ML competitions
- [Open Data on AWS](https://registry.opendata.aws/): 100+ large-scale raw(原始) data
- Data lakes in your own organization

### Data integration(集成)

- Combine(联合) data from multiple sources into a coherent dataset
- Product data is often stored in multiple tables
  - E.g. a table for house information, a table for sales, a table for listing agents(代理人)
- Join tables by keys, which are often entity(实体) IDs
- Key issues: identify IDs, missing rows, redundant(冗余) columns, value conflicts(冲突)

### Summary

- Finding the right data is challenging 
- Raw data in industrial settings VS academic datasets
- Data integration combines data from multiple sources
- Synthesizing(合成) data is getting popular
- Data augmentation(增强) a common practice



## 1.3 Web Scraping(抓取)

### Web scraping tools

- "curl" often doesn't work

  - Website owners use various ways to stop bots

- Use headless(无头的) browser(浏览器): a web browser without a GUI

  ```python
  # 抓取网页
  from selenium import webdriver
  from selenium.webdriver.chrome.service import Service
  
  service = Service(
      r"D:\dfh\chromedriver\chromedriver.exe"
  )
  chrome_options = webdriver.ChromeOptions()
  chrome_options.headless = True
  chrome = webdriver.Chrome(service=service,options=chrome_options)
  
  chrome.get("https://quotes.toscrape.com/")
  print(chrome.title)
  ```

- You need a lot of new IPs, easy to get through public clouds

  - In all IPv4 IPs, AWS owns 1.75%, Azure 0.55%, GCP 0.25%

### Summary

- Web scraping is a powerful way to collect data at scale(规模) when the website doesn't offer a data API
- Low cost if using public clouds
- Use browser's inspection(检查) tool to locate(定位) the information in HTML
- Be cautious(慎重的) to use it properly(适当地)

## 1.4 Data Labeling(标注)