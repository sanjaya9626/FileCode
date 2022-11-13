class ImportTemplateAPIView(generics.GenericAPIView):
    """ Import Template API view """
    lookup_field = "importtemplate_id"

    def post(self, request, *args, **kwargs):
        """ Import Template API view : POST method """
        
        data = request.data
        try:
            allowed_mime = [
                    "text/plain"
                ]
            try:
                content_type = mimetypes.guess_type(
                        data.get("fileUrl").name
                    )[0]

            except Exception :
                   content_type = None

                if not data.get("fileUrl"):
                    return Response(
                        {
                            "message": "Select a valid file ( "text/plain" ).",
                            "api_status": 0,
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                if content_type and content_type in allowed_mime:
                    delimeter = data.get("delimeter")
                    filepath = str(data.get("fileUrl"))
                    filepathArray = str(filepath).split(".")
                    typeArray = ["csv", "xls", "xlsx"]
                    file_name = filepath.split("/")[-1]
                    try:
                        extn = file_name.split(".")[-1]

                        if not len(filepathArray):
                            errors.append("Invalid Path")
                        else:
                            if extn not in typeArray:
                                errors.append(
                                    extn
                                    + " Invalid file type. File must be of type csv, xls, xlsx."
                                )
                    except Exception:
                        pass

                    if len(errors) > 0:
                        error_txt = ". ".join([str(i) for i in errors])
                        return Response(
                            {"message": error_txt, "api_status": 0},
                            status=status.HTTP_400_BAD_REQUEST,
                        )

                    body_data["excess_row_in_progress"] = 0
                    if extn == "csv":
                    try:
                       csvReader = csv.reader(
                       codecs.open(
                                settings.MEDIA_ROOT
                                + uploaded_file_url,
                                 "r",
                                            encoding=file_encoading,
                                            errors="ignore",
                                        ),
                                        delimiter=delimeter,
                                    )
                                    if csvReader == "":
                                        errors.append(
                                            "Please Import Utf-8 File."
                                        )
                                    else:
                                        reader = list(csvReader)
                                    for row in reader:
                                        if rec_count == 0:
                                            xls_column_header_obj = row
                                            xls_column_header_row_obj = dict()
                                            for key in xls_column_header_obj:
                                                xls_column_header_row_obj[key] = key
                                            xls_data_info.append(xls_column_header_row_obj)

                                        elif rec_count <=import_batch_limit:
                                            xls_data_info_obj = dict(
                                                zip(xls_column_header_obj, row)
                                            )
                                            xls_data_info.append(
                                                xls_data_info_obj
                                            )
                                        else:
                                            thread_argument.update({"header_row":xls_column_header_row_obj})
                                            body_data["excess_row_in_progress"] = 1
                                            break
                                        rec_count = rec_count + 1
                                except Exception as e:
                                    errors.append(repr(e))
                            elif extn == "xls" or extn == "xlsx":
                                try:
                                    wb = open_workbook(
                                        settings.MEDIA_ROOT + uploaded_file_url
                                    )
                                    for s in wb.sheets():
                                        values = []
                                        for row in range(s.nrows):
                                            if rec_count <=import_batch_limit:
                                                col_value = []
                                                for col in range(s.ncols):
                                                    (
                                                        value,
                                                        value_type,
                                                    ) = data_type_check(
                                                        s.cell(row, col).value
                                                    )

                                                    col_value.append(str(value))
                                                values.append(col_value)
                                                row = values[0]
                                                xls_data_info_obj = dict(
                                                    zip(row, col_value)
                                                )
                                                xls_data_info.append(
                                                    xls_data_info_obj
                                                )
                                            else:
                                                thread_argument.update({"header_row":values[0]})
                                                body_data["excess_row_in_progress"] = 1
                                                break
                                            
                                            rec_count += 1
                                except Exception as e:
                                    errors.append(repr(e))

                            if len(xls_data_info) == 1:
                                errors.append("Uploaded file is empty.")
                            else:
                                for coldata in xls_data_info[0]:
                                    if coldata.lower() != "item name":
                                        try:
                                            mappobj = ImportTemplateMapper.objects.filter(
                                                importtemplate_id=import_save.importtemplate_id,
                                                templatefield_name=coldata.strip(),
                                            ).first()
                                        except ImportTemplateMapper.DoesNotExist:
                                            mappobj = None

                                        if mappobj:
                                            tempmapperserializer = (
                                                ImportTemplateMapperSerializer(
                                                    mappobj
                                                )
                                            )
                                            mapdata.append(
                                                tempmapperserializer.data
                                            )
                                        else:
                                            mapjsondata = {
                                                "importtemplate": import_save.importtemplate_id,
                                                "templatefield_name": coldata,
                                                "databasefield_name": "",
                                                "field_description": "",
                                                "is_required": False,
                                                "is_set": False,
                                            }
                                            tempmapperserializer = (
                                                ImportTemplateMapperSerializer(
                                                    data=mapjsondata
                                                )
                                            )
                                            if tempmapperserializer.is_valid():
                                                tempmapperserializer.save()
                                                mapdata.append(
                                                    tempmapperserializer.data
                                                )
                                            else:
                                                transaction.set_rollback(True)
                                                return Response(
                                                    {
                                                        "message": tempmapperserializer.errors,
                                                        "api_status": 0,
                                                    },
                                                    status=status.HTTP_400_BAD_REQUEST,
                                                )
                                                
                            body_data["mapdata"] = mapdata

                    else:
                        transaction.set_rollback(True)
                        err = self.errorformat(
                            errormsg=repr(import_data.errors)
                        )
                        return Response(
                            {"message": err, "api_status": 0},
                            status=status.HTTP_400_BAD_REQUEST,
                        )

                else:
                    return Response(
                        {
                            "message": "Invalid File type. Select a valid file ( csv, xls, xlsx ).",
                            "api_status": 0,
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                if len(errors) > 0:
                    error_txt_final = ". ".join([str(i) for i in errors])
                    return Response(
                        {"message": error_txt_final, "api_status": 0},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                body_data["import_data"] = xls_data_info
                body_data["total_rows"] = len(xls_data_info)
                body_data["valid_count"] = len(xls_data_info)
                body_data["error_count"] = 0
                body_data["warning_count"] = 0
                body_data["importsuccess_rows"] = 0
                body_data["id"] = import_save.importtemplate_id
                body_data["taxonomy_name"] = taxonomy_name  
                resp_data = ElasticSearchInstance.get_record_by_id(index=EsIndexTemplate,id=import_save.importtemplate_id)  
                if resp_data["found"] and "last_validated_rows" in resp_data["data"]:
                    body_data["last_validated_rows"] = resp_data["data"]["last_validated_rows"]
                else:
                    body_data["last_validated_rows"] = []      
                if resp_data["found"] and "import_exception" in resp_data["data"]:
                    body_data["last_import_exception"] = resp_data["data"]["import_exception"]
                else:
                    body_data["last_import_exception"] = []   
                es.index(
                    index=EsIndexTemplate,
                    doc_type=doc_type,
                    id=import_save.importtemplate_id,
                    body=body_data,
                )
                body_data["fileUrl"] = ""
                if "header_row" in thread_argument and thread_argument["header_row"]:
                    self.get_rows_from_file(self,**thread_argument)

            except Exception as e:
                transaction.set_rollback(True)
                err = self.errorformat(errormsg=repr(e))
                return Response(
                    {"message": err, "api_status": 0},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(body_data, status=status.HTTP_201_CREATED)
