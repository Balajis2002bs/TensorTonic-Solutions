def compute_monitoring_metrics(system_type: str, y_true: list, y_pred: list) -> dict:
    """
    Returns a dictionary of metrics.
    """
    # Write code here
    if system_type == 'classification':
        tp,tn,fp,fn=0,0,0,0
        for i in range(len(y_true)):
           
            if  y_true[i]==1 and y_pred[i]==1:
                tp+=1
            elif y_true[i]==0 and y_pred[i]==0:
                    tn+=1
            
            elif y_true[i]==1 and y_pred[i]==0:
    
                fn+=1
            elif y_true[i]==0 and y_pred[i]==1:
    
                fp+=1

            print(tp,tn,fp,fn)
            try: 
                accuracy=round((tp+tn)/(tp+tn+fp+fn),3)
                precision=round(tp/(tp+fp),3)
                recall=round(tp/(tp+fn),3)
                f1_score=round((2*precision * recall)/(precision+recall),3)
            except ZeroDivisionError:
                precision=0
                recall=0
                f1_score=0
            metric_report={
                "accuracy": accuracy,
                "precision": precision,
                "recall": recall,
                "f1":f1_score
            }
            
            
            
    elif system_type=='regression':
        sum,sqr_sum=0,0
        for i in range(len(y_true)):
            sum += abs(y_true[i]-y_pred[i])
            sqr_sum += (y_true[i]-y_pred[i]) ** 2
            mae=sum/len(y_true)
            rmse=sqr_sum/len(y_true)
            rmse=(rmse)**0.5
        metric_report={
            "mae": mae,
            "rmse": rmse
        }



    elif system_type == 'ranking':
        ranked = sorted(
            zip(y_true, y_pred),
            key=lambda x: x[1],
            reverse=True
        )
        top_3=ranked[:3]
        P,R=0,0
        for actual_item,_ in top_3:
            if actual_item == 1:
                P += 1
                R += 1
        P=P/3
        R=R/3
        metric_report={
            "precision_at_3": P,
            "recall_at_3": R
        }
            
        
        
    return metric_report
            
            
        
    