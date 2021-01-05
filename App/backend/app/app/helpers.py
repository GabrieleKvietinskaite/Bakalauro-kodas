def calculateAverage(data):
    sum = calculateSum(data)

    return int(sum/len(data))

def calculateResults(availability_data, business_data, defence_data, reports_data, other_data):
    return (calculateAverage(availability_data) * 0.45 +
        calculateAverage(business_data) * 0.2 +
        calculateAverage(defence_data) * 0.2 +
        calculateAverage(reports_data) * 0.1 +
        calculateAverage(other_data) * 0.05)

def calculateLevelPass(hypothesis_data, level):
    hyp_sum = calculateSum(hypothesis_data)
    
    if hyp_sum > level.points_to/2:
        return True
    else:
        return False

def calculateSum(data):
    sum = 0

    for x in data:
        sum += x

    return round(sum, 5)

def split_to_float_array(data, split_by):
    if len(data) > 0:
        return [float(x) for x in data.split(split_by)]
    return [0]

def check(databas, request):
    if not databas:
        return request
    else:
        return databas + ';' + request