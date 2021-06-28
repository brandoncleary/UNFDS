#!/usr/bin/env python
# coding: utf-8

# Write a 1-2 page report summarizing your recommendations for Big Mountain Resort. Be sure to include the figures you created to back up your recommendations.

# The two kinds of ticket prices, Adult weekend price and adult weekday price, were utilized to price a model to maximize returns of Big Mountain Resort in Montana.
# 
# There is a positive correlation between the ratio of night skiing area with the number of resorts per capita. It seems that when resorts are more densely located with population, more night skiing is provided.
# 
# Turning your attention to your target feature, AdultWeekend ticket price, you see quite a few reasonable correlations. fastQuads stands out, along with Runs and Snow Making_ac. The last one is interesting. Visitors would seem to value more guaranteed snow, which would cost in terms of snow making equipment, which would drive prices and costs up. Of the new features, resort_night_skiing_state_ratio seems the most correlated with ticket price. If this is true, then perhaps seizing a greater share of night skiing capacity is positive for the price a resort can charge.
# 
# As well as Runs, total_chairs is quite well correlated with ticket price. This is plausible; the more runs you have, the more chairs you'd need to ferry people to them! Interestingly, they may count for more than the total skiable terrain area. For sure, the total skiable terrain area is not as useful as the area with snow making. People seem to put more value in guaranteed snow cover rather than more variable terrain area.
# 
# The vertical drop seems to be a selling point that raises ticket prices as well.
# 
# 
# At first these relationships are quite counterintuitive. It seems that the more chairs a resort has to move people around, relative to the number of runs, ticket price rapidly plummets and stays low. What we may be seeing here is an 
# exclusive vs. mass market resort effect; if you don't have so many chairs, you can charge more for your tickets, although with fewer chairs you're inevitably going to be able to serve fewer visitors. Your price per visitor is high but your number of visitors may be low. Something very useful that's missing from the data is the number of visitors per year.
# 
# It also appears that having no fast quads may limit the ticket price, but if your resort covers a wide area then getting a small number of fast quads may be beneficial to ticket price.
# 
# linear model coefficients
# vertical_drop        10.767857
# Snow Making_ac        6.290074
# total_chairs          5.794156
# fastQuads             5.745626
# Runs                  5.370555
# LongestRun_mi         0.181814
# trams                -4.142024
# SkiableTerrain_ac    -5.249780
# dtype: float64
# 
# These results suggest that vertical drop is your biggest positive feature. This makes intuitive sense and is consistent with what you saw during the EDA work. Also, you see the area covered by snow making equipment is a strong positive as well. People like guaranteed skiing! The skiable terrain area is negatively associated with ticket price! This seems odd. People will pay less for larger resorts? There could be all manner of reasons for this. It could be an effect whereby larger resorts can host more visitors at any one time and so can charge less per ticket. As has been mentioned previously, the data are missing information about visitor numbers. Bear in mind, the coefficient for skiable terrain is negative for this model. For example, if you kept the total number of chairs and fastQuads constant, but increased the skiable terrain extent, you might imagine the resort is worse off because the chairlift capacity is stretched thinner.
# 
# 
# Random Forest top four features:
# fastQuads
# Runs
# Snow Making_ac
# vertical_drop
# 
# The random forest model has a lower cross-validation mean absolute error by almost \$1. It also exhibits less variability. Verifying performance on the test set produces performance consistent with the cross-validation results. There seems to be sufficient data. There's an initial rapid improvement in model scores as one would expect, but it's essentially levelled off by around a sample size of 40-50.
# 
# Big Mountain Resort modelled price is $95.87, actual price is $81.00.
# Even with the expected mean absolute error of $10.39, this suggests there is room for an increase. This result should be looked at optimistically and doubtfully! The validity of our model lies in the assumption that other resorts accurately set their prices according to what the market (the ticket-buying public) supports. The fact that our resort seems to be charging that much less that what's predicted suggests our resort might be undercharging. But if ours is mispricing itself, are others? It's reasonable to expect that some resorts will be "overpriced" and some "underpriced." Or if resorts are pretty good at pricing strategies, it could be that our model is simply lacking some key data? Certainly we know nothing about operating costs, for example, and they would surely help.
# 
# potential scenarios:
# Scenario 1:The model says closing one run makes no difference.
# Scenario 2:This scenario increases support for ticket price by $1.99.Over the season, this could be expected to amount to $3474638.
# Scenario 3: The additional acres are insignificant. Just go with scenario 2 because it will be easier to implement.
# Scenario 4: No difference.
# 
# In conclusion, my recommendations for Big Mountain Resort in Montana include, but are not limited to, raising its prices to $97.86, closing its least used run, adding a run, increasing the vertical drop by 150 feet, and installing an additional chair lift.
# 
