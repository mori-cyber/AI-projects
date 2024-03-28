wandb.watch(model)

for epoch in range(config.epochs):
    train_loss = 0.0
    train_acc = 0.0
    for images, labels in tqdm(test_data_loader):
        images, labels = images.to(device), labels.to(device)
        # print(images.shape)
        optimizer.zero_grad()
        # images = images.float()
        preds = model(images)

        loss = loss_function(preds, labels)
        loss.backward()

        optimizer.step()

        test_loss += loss
        test_acc += calc_acc(preds, labels)

    total_loss = test_loss / len(test_data_loader)
    total_acc = test_acc / len(test_data_loader)
    if epoch % 2 == 0:
        wandb.log({"loss": total_loss})
        wandb.log({"acc": total_acc})

    # total_acc = train_acc/len(train_data_loader)
    print(f"Epoch:{epoch}: Loss:{total_loss}, Acc:{total_acc}")

    print("-------------------------------------")