# kafka
```
> sudo apt-get install kafkacat
> pip install kafka-tools

> kafka-tools -b IP:PORT print_topics - все топики
> kafka-tools -b IP:PORT desc_topic <topicName> - топик инфо
> kafka-tools -b IP:PORT consume_topic <topicName> - подписаться на топик, получить вывод всех месседжей
> kt consume -brokers IP -topic <topicName> - подписаться на топик, получить вывод всех месседжей
```
