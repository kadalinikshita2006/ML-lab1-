
payments =[386, 289, 393, 110, 280, 167, 271, 274, 148, 198]
for i,payments in enumerate(payments,1):
    if payments>200:
        status="rich"
    else: 
        status="poor"
    print(f"customer {i} is classified as {status}")